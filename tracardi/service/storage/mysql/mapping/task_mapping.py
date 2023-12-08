from tracardi.context import get_context
from tracardi.domain.task import Task
from tracardi.service.storage.mysql.schema.table import TaskTable
from tracardi.service.storage.mysql.utils.serilizer import from_json, to_json


def map_to_task_table(task: Task) -> TaskTable:
    context = get_context()

    return TaskTable(
        id=task.id,
        tenant=context.tenant,
        production=context.production,
        timestamp=task.timestamp,
        status=task.status,
        name=task.name,
        type=task.type,
        progress=task.progress,
        task_id=task.task_id,
        params=to_json(task.params),
    )


def map_to_task(task_table: TaskTable) -> Task:
    return Task(
        id=task_table.id,
        timestamp=task_table.timestamp,
        status=task_table.status,
        name=task_table.name,
        type=task_table.type,
        progress=task_table.progress,
        task_id=task_table.task_id,
        params=from_json(task_table.params),
    )
