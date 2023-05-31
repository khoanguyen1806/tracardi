from typing import Tuple

from tracardi.context import ServerContext, Context, get_context
from tracardi.service.storage.indices_manager import get_indices_status


def get_missing(indices, type) -> list:
    return [idx[1] for idx in indices if idx[0] == type]


async def is_schema_ok() -> Tuple[bool, list]:

    # Missing indices in staging
    with ServerContext(get_context().switch_context(production=False)):
        print('B123 install', get_context())
        _indices_staging = [item async for item in get_indices_status()]

    # Missing indices in production
    with ServerContext(get_context().switch_context(production=True)):
        print('B124 install', get_context())
        _indices_production = [item async for item in get_indices_status()]

    _indices = _indices_staging + _indices_production

    missing_indices = get_missing(_indices, type='missing_index')
    missing_aliases = get_missing(_indices, type='missing_alias')

    is_schema_ok = not missing_indices and not missing_aliases

    return is_schema_ok, _indices
