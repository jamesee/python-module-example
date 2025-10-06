
def hello() -> str:
    return "Hello from ech-module!"

from .cal import add, subtract, multiply, divide
__all__ = ["hello", "add", "subtract", "multiply", "divide" ]
