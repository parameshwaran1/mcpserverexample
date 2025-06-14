## Installation Steps for Deployable MCP Server

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
