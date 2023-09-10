import logging
import redis
from abc import ABC, abstractmethod

from tracardi.service.license import License, VALIDATOR
from tracardi.domain.profile import Profile
from tracardi.domain.tracker_payloads import TrackerPayloads
from tracardi.exceptions.exception import TracardiException
from tracardi.domain.payload.tracker_payload import TrackerPayload
from tracardi.service.notation.dot_accessor import DotAccessor
from tracardi.service.storage.driver.elastic import profile as profile_db
from tracardi.service.storage.driver.elastic import session as session_db
from tracardi.service.synchronizer import profile_synchronizer
from tracardi.service.tracker_config import TrackerConfig
from tracardi.config import tracardi
from tracardi.domain.event_source import EventSource
from tracardi.exceptions.log_handler import log_handler
from typing import List, Callable, Coroutine, Any, Type
from tracardi.domain.value_object.collect_result import CollectResult
from tracardi.service.console_log import ConsoleLog
from tracardi.service.tracker_persister import TrackerResultPersister
from tracardi.service.tracking.event_validation import validate_events
from tracardi.service.tracking_manager import TrackerResult, TrackingManagerBase
from tracardi.service.tracking_orchestrator import TrackingOrchestrator

if tracardi.enable_event_validation and License.has_service(VALIDATOR):
    from com_tracardi.service.tracker_event_reshaper import EventsReshaper


logger = logging.getLogger(__name__)
logger.setLevel(tracardi.logging_level)
logger.addHandler(log_handler)


class TrackProcessorBase(ABC):

    def __init__(self,
                 console_log: ConsoleLog,
                 on_profile_merge: Callable[[Profile], Profile] = None,
                 on_profile_ready: Type[TrackingManagerBase] = None,
                 on_result_ready: Callable[[List[TrackerResult], ConsoleLog], Coroutine[Any, Any, CollectResult]] = None):

        self.on_profile_ready = on_profile_ready
        self.on_profile_merge = on_profile_merge
        self.console_log = console_log
        self.on_result_ready = on_result_ready

    @abstractmethod
    async def handle(self,
                     tracker_payloads: TrackerPayloads,
                     source: EventSource,
                     tracker_config: TrackerConfig) -> List[CollectResult]:
        pass


class TrackerProcessor(TrackProcessorBase):

    @staticmethod
    async def _handle_on_result_ready(tracker_results, console_log) -> CollectResult:
        tp = TrackerResultPersister(console_log)
        return await tp.persist(tracker_results)

    async def handle(self,
                     tracker_payloads: TrackerPayloads,
                     source: EventSource,
                     tracker_config: TrackerConfig) -> List[CollectResult]:

        """
        Starts collecting data and process it.
        """
        responses = []

        try:

            # Use redis to lock profile

            orchestrator = TrackingOrchestrator(
                source,
                tracker_config,
                on_profile_merge=self.on_profile_merge,
                on_profile_ready=self.on_profile_ready
            )

            tracker_results: List[TrackerResult] = []
            debugging: List[TrackerPayload] = []

            for tracker_payload in tracker_payloads:

                # if no events in payload continue

                if not tracker_payload.events:
                    continue

                if tracardi.enable_event_validation and License.has_service(VALIDATOR):
                    # Validate events. Checks validators and its conditions and sets validation status.

                    # Event payload will be filled with validation status. Mutates tracker_payload
                    tracker_payload = await validate_events(tracker_payload)

                    # Reshape valid events

                    evh = EventsReshaper(tracker_payload)
                    tracker_payload = await evh.reshape_events()

                # Locks for processing each profile
                result = await orchestrator.invoke(tracker_payload, self.console_log)
                tracker_results.append(result)
                responses.append(result.get_response_body(tracker_payload.get_id()))
                debugging.append(tracker_payload)

                # Save bulk

                if self.on_result_ready is None:
                    save_results = await self._handle_on_result_ready(tracker_results, self.console_log)
                else:
                    save_results = await self.on_result_ready(tracker_results, self.console_log)

                # UnLock profile

                if orchestrator.locked and source.synchronize_profiles:
                    profile_synchronizer.unlock_entities(orchestrator.locked)
                    if tracardi.enable_profile_immediate_flush:
                        await profile_db.refresh()
                        await session_db.refresh()

                logger.debug(f"Invoke save results {save_results} tracker payloads.")

                # Debugging rest

                if tracardi.track_debug:
                    responses = save_results.get_debugging_info(responses, debugging)

        except redis.exceptions.ConnectionError as e:
            raise TracardiException(f"Could not connect to Redis server. Connection returned error {str(e)}")

        logger.info(f"Track responses {responses}.")
        if len(responses) == 1:
            return responses[0]
        return responses
