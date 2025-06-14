# MCP Create Server

[![NPM version](http://img.shields.io/npm/v/mcp.svg?style=flat-square)](https://www.npmjs.org/package/mcp)

A dynamic MCP server management service that creates, runs, and manages Model Context Protocol (MCP) servers dynamically. This service itself functions as an MCP server and launches/manages other MCP servers as child processes, enabling a flexible MCP ecosystem.

<a href="https://glama.ai/mcp/servers/@parameshwaran1/mcpserverexample">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@parameshwaran1/mcpserverexample/badge" alt="Deployable Server MCP server" />
</a>

## Installation Steps for Deployable MCP Server
###
To install and run the Deployable MCP Server, use the following command:

```
uvx --from https://github.com/parameshwaran1/mcpserverexample.git mcp-server
```

Or, in JSON configuration format:

```
"Deployable MCP Server": {
  "command": "uvx",
  "args": [
    "--from",
    "https://github.com/parameshwaran1/mcpserverexample.git",
    "mcp-server"
  ]
}
```

## Usage

After installation, you can start the MCP server using the command:

```
uvx --from https://github.com/parameshwaran1/mcpserverexample.git mcp-server
```

This will launch the Deployable MCP Server, making its tools available for use.

## Features
- Simple addition tool: Adds two integers and returns the result.
- Easily extendable: Add more tools by defining new functions with docstrings.

## Requirements
- Python 3.8+
- `uv` and `uvx` installed. You can install them with:
  ```
  pip install uv
  pip install uvx
  ```

## Contributing
Feel free to fork the repository and submit pull requests for new features or bug fixes.

## License
This project is licensed under the MIT License.