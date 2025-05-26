from mcp import Server, McpError
from mcp.types import Resource, Tool
import asyncio

# Create server instance
server = Server("my-server")

@server.list_resources()
async def list_resources():
    return [
        Resource(
            uri="file://example.txt",
            name="Example File",
            mimeType="text/plain"
        )
    ]

@server.read_resource()
async def read_resource(uri: str):
    if uri == "file://example.txt":
        return "Hello, World!"
    raise McpError(f"Resource not found: {uri}")

if __name__ == "__main__":
    asyncio.run(server.run())def main():
    print("Hello from mcp-server!")


if __name__ == "__main__":
    main()
