def hello_world():
    return "Hello from Hermes Pipeline"


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def subtract(a: int | float, b: int | float) -> int | float:
    return a - b


def divide(a, b) -> float:
    if b == 0:
        raise ValueError("division by zero")
    return a / b