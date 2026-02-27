from typing import Dict
from exceptions import InfrastructureError
from schemas import Task


class TaskRepository:

    def __init__(self):
        self._storage: Dict[int, Task] = {}

    def save(self, task: Task):
        try:
            self._storage[task.id] = task
        except Exception as e:
            raise InfrastructureError("Failed to save task") from e

    def get_by_id(self, task_id: int):
        return self._storage.get(task_id)

    def list_all(self):
        return list(self._storage.values())
