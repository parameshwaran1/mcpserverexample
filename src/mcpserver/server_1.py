from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Deployable MCP Server")

@mcp.tool()
def add(i:int , j:int) -> int:
    """
    Adds two integers and returns the result.
    
    Args:
        i (int): The first integer to add.
        j (int): The second integer to add.
    
    Returns:
        int: The sum of i and j.
    """
    return i+ j

