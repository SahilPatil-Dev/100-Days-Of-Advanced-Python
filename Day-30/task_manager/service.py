from schemas import Task
from validators import validate_task_input
from exceptions import NotFoundError


class TaskService:

    def __init__(self, repository):
        self._repository = repository
        self._next_id = 1

    def create_task(self, title: str):
        validate_task_input(title)
        task = Task(id=self._next_id, title=title)
        self._repository.save(task)
        self._next_id += 1
        return task

    def complete_task(self, task_id: int):
        task = self._repository.get_by_id(task_id)
        if not task:
            raise NotFoundError("Task not found")

        task.completed = True
        return task

    def get_task(self, task_id: int):
        task = self._repository.get_by_id(task_id)
        if not task:
            raise NotFoundError("Task not found")
        return task

    def list_tasks(self):
        return self._repository.list_all()
