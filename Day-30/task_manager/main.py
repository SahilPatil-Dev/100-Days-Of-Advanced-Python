from repository import TaskRepository
from service import TaskService
from exceptions import AppError
from response import success_response, handle_exception


def main():

    repo = TaskRepository()
    service = TaskService(repo)

    try:
        # Create multiple tasks
        task1 = service.create_task("Learn backend architecture")
        task2 = service.create_task("Learn through consistency")

        print(success_response(task1.__dict__))
        print(success_response(task2.__dict__))

        # Complete task using returned ID
        completed = service.complete_task(task1.id)
        print("\nTask Completed using returned ID: ")
        print(success_response(completed.__dict__))

        # List all tasks
        tasks = service.list_tasks()
        print("\nList of the Tasks: ")
        print(success_response([t.__dict__ for t in tasks]))

    except AppError as e:
        print(handle_exception(e))


if __name__ == "__main__":
    main()
