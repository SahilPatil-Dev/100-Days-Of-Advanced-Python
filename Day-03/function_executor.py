def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b


OPERATIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply
}


def execute_operation(operation_name, a, b):
    if operation_name not in OPERATIONS:
        raise ValueError("Invalid operation")

    operation_func = OPERATIONS[operation_name]
    return operation_func(a, b)


print(execute_operation("add", 5, 3))
print(execute_operation("multiply", 4, 6))
