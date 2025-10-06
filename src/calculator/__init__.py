from .cal import add, subtract, multiply, divide


def hello() -> str:
    return "Hello from ech-module!"


__all__ = ["hello", "add", "subtract", "multiply", "divide"]
