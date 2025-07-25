# MCP (Model Context Protocol) Integration

This browser agent now includes full support for the Model Context Protocol (MCP), allowing you to extend its capabilities with external tools and services.

## What is MCP?

The Model Context Protocol (MCP) is an open standard that enables AI assistants to securely connect to external data sources and tools. It allows the agent to:

- Access filesystems, databases, and APIs
- Use specialized tools for different domains
- Connect to community-developed servers
- Extend functionality without code changes

## Features

### 🔌 One-Button MCP Access
- Click the "🔌 MCP" button in the chat interface for quick access
- Interactive menu for common MCP operations
- Direct command input support

### 🛠️ MCP Marketplace
- Browse and install MCP servers from the marketplace
- Featured servers for common use cases
- Community-contributed servers
- Easy server management (install, uninstall, enable, disable)

### 💬 Chat Integration
- Natural language MCP commands
- Automatic tool suggestions
- Seamless integration with browser automation

## Quick Start

### 1. Access MCP Features

**Via Chat Commands:**
```
/mcp help                    # Show all MCP commands
/mcp list_tools             # List available tools
/mcp status                 # Show connection status
/mcp connect filesystem     # Connect to filesystem server
```

**Via MCP Button:**
- Click the "🔌 MCP" button in the chat
- Select from the interactive menu
- Or type commands directly

**Via MCP Tab:**
- Go to the "MCP" tab in the main window
- Browse the marketplace
- Manage installed servers
- Test tools

### 2. Popular MCP Servers

**Filesystem Server:**
```
/mcp connect filesystem
/mcp call_tool read_file --path "/path/to/file.txt"
```

**Database Server:**
```
/mcp connect sqlite
/mcp call_tool query --sql "SELECT * FROM users"
```

**Web Search Server:**
```
/mcp connect brave-search
/mcp call_tool search --query "latest AI news"
```

## Available Commands

### Server Management
- `/mcp servers` - List all servers
- `/mcp connect <server_name>` - Connect to a server
- `/mcp disconnect <server_name>` - Disconnect from a server
- `/mcp status` - Show connection status

### Tool Operations
- `/mcp list_tools` - List available tools
- `/mcp call_tool <tool_name> [args]` - Call a specific tool
- `/mcp tool_info <tool_name>` - Get tool information

### Resource Management
- `/mcp list_resources` - List available resources
- `/mcp read_resource <uri>` - Read a resource

### Help
- `/mcp help` - Show all commands
- `/mcp help <command>` - Get help for specific command

## Natural Language Integration

You can also use natural language to interact with MCP:

```
"List available MCP tools"
"Use MCP to read the file config.json"
"Connect to the filesystem server"
"Show me what MCP servers are available"
```

## Installing New Servers

### Via Marketplace (Recommended)
1. Go to the MCP tab
2. Browse available servers
3. Click "Install" on desired servers
4. Enable and connect

### Manual Installation
1. Add server configuration to `mcp_servers.json`
2. Restart the application
3. Connect via `/mcp connect <server_name>`

## Example Workflows

### File Operations
```
# Connect to filesystem
/mcp connect filesystem

# Read a file
/mcp call_tool read_file --path "./config.json"

# Write to a file
/mcp call_tool write_file --path "./output.txt" --content "Hello MCP!"

# List directory contents
/mcp call_tool list_directory --path "./"
```

### Database Operations
```
# Connect to SQLite
/mcp connect sqlite

# Query data
/mcp call_tool query --sql "SELECT name, email FROM users LIMIT 10"

# Execute commands
/mcp call_tool execute --sql "UPDATE users SET status='active' WHERE id=1"
```

### Web Integration
```
# Search the web
/mcp connect brave-search
/mcp call_tool search --query "Python MCP examples"

# Combine with browser automation
"Search for 'MCP servers' using MCP, then navigate to the first result"
```

## Troubleshooting

### Common Issues

**Server Won't Connect:**
- Check if the server is properly installed
- Verify the server configuration
- Check the logs in the MCP tab

**Tool Not Found:**
- Ensure the server is connected
- Use `/mcp list_tools` to see available tools
- Check tool name spelling

**Permission Errors:**
- Some tools require specific permissions
- Check file/directory access rights
- Run with appropriate privileges if needed

### Getting Help

1. Use `/mcp help` for command reference
2. Check the MCP tab for server status
3. Review error messages in the chat
4. Consult server-specific documentation

## Advanced Configuration

### Custom Server Configuration

Edit `mcp_servers.json` to add custom servers:

```json
{
  "my_custom_server": {
    "name": "My Custom Server",
    "description": "Custom MCP server",
    "command": "python",
    "args": ["/path/to/server.py"],
    "env": {
      "API_KEY": "your_api_key"
    }
  }
}
```

### Environment Variables

Some servers require environment variables:
- Set them in your system environment
- Or add them to the server configuration
- Use `.env` file for sensitive data

## Security Considerations

- MCP servers run as separate processes
- File access is limited to configured paths
- Network access depends on server implementation
- Review server code before installation
- Use trusted sources for servers

## Contributing

To contribute MCP servers or improvements:
1. Follow MCP specification standards
2. Test thoroughly with the browser agent
3. Document usage and requirements
4. Submit to the community marketplace

---

**Need Help?** Use `/mcp help` in the chat or check the MCP tab for more information.