"""
Tavily MCP Server with Proxy Support
"""

from mcp_server_tavily.server import serve

__version__ = "0.1.0"

def main():
    """Entry point for the application."""
    import asyncio
    import os
    import sys
    
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        print("Error: TAVILY_API_KEY environment variable is required", file=sys.stderr)
        sys.exit(1)
        
    asyncio.run(serve(api_key))