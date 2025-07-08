# server.py
from mcp.server.fastmcp import FastMCP
from datetime import datetime

print ("Starting Demo MCP server...")
# Create an MCP server
mcp = FastMCP("Demo")

# Add a function that returns a string with "Gon" prefix and current time
@mcp.tool()
def getfunctionnametime() -> str:
    """Return string with Gon prefix followed by current time in HHMMSS format"""
    current_time = datetime.now().strftime("%H%M%S")
    result = f"Gon{current_time}"
    print(f"Generated function name: {result}")
    return result


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print(f"Adding {a} and {b}")
    return a + b * 2


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"