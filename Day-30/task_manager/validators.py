from exceptions import ValidationError


def validate_task_input(title: str):
    if not title or not isinstance(title, str):
        raise ValidationError("Task title must be a non-empty string")
