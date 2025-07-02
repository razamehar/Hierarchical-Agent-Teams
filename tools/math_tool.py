from langchain_core.tools import tool


@tool
def add_tool(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b

@tool
def subtract_tool(a: float, b: float) -> float:
    """Subtract two numbers"""
    return a - b

@tool
def multiply_tool(a: float, b: float):
    """Multiply two numbers"""
    return a * b

@tool
def divide_tool(a: float, b: float):
    """Divide two numbers, return 'Infinity' if divided by zero"""
    if b == 0:
        return float('inf')
    return a / b

