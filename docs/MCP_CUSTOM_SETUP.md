# Custom MCP Server Setup Guide

This guide explains how to set up and use the custom MCP (Model Context Protocol) servers configured for Browser Agent, including the n8n-mcp, cursor-talk-to-figma-mcp, and our custom Browser Agent MCP server.

## Overview

The Browser Agent project now includes three custom MCP servers:

1. **n8n-mcp** - Workflow automation integration
2. **cursor-talk-to-figma-mcp** - Figma design automation
3. **brouser-agent-custom-mcp** - Enhanced browser automation capabilities

## Configuration Files

### Main Configuration
- **mcp_servers.json** - Primary MCP server configuration file
- **mcp_custom_server.py** - Custom MCP server implementation
- **.brouser_agent_status** - Updated with MCP configuration status

## Installation Instructions

### 1. N8N MCP Server

**Purpose**: Provides comprehensive access to n8n node documentation, properties, and operations for building workflows.

**Installation**:
```bash
# Install n8n-mcp globally
npm install -g n8n-mcp

# Or use npx (recommended)
npx n8n-mcp
```

**Environment Variables**:
```bash
export N8N_API_URL="https://your-n8n-instance.com/api/v1"
export N8N_API_KEY="your-n8n-api-key"
export MCP_MODE="stdio"
export LOG_LEVEL="error"
export DISABLE_CONSOLE_OUTPUT="true"
```

**Features**:
- Access to n8n node documentation
- Workflow creation and management
- Node property configuration
- Automation workflow building

### 2. Cursor Talk to Figma MCP

**Purpose**: Enables communication with Figma for reading designs and modifying them programmatically.

**Installation**:
```bash
# Install using Bun (recommended)
bun install cursor-talk-to-figma-mcp

# Or use bunx
bunx cursor-talk-to-figma-mcp@latest
```

**Environment Variables**:
```bash
export FIGMA_ACCESS_TOKEN="your-figma-access-token"
export WEBSOCKET_URL="ws://localhost:3001"
```

**Getting Figma Access Token**:
1. Go to Figma → Settings → Account → Personal Access Tokens
2. Generate a new token with appropriate permissions
3. Copy the token and set it as FIGMA_ACCESS_TOKEN

**Features**:
- Read Figma designs and components
- Modify design elements programmatically
- Extract design tokens and assets
- Automate design workflows

### 3. Browser Agent Custom MCP Server

**Purpose**: Custom implementation providing enhanced browser automation, AI processing, and task management.

**Installation**:
```bash
# Install MCP SDK
pip install mcp

# The server is already implemented in mcp_custom_server.py
# Make it executable
chmod +x mcp_custom_server.py
```

**Environment Variables**:
```bash
export BROUSER_AGENT_API_KEY="your-api-key"
export CUSTOM_MCP_PORT="8080"
export LOG_LEVEL="INFO"
```

**Features**:
- Browser automation task creation and management
- AI-powered content analysis
- Session management for multiple browsers
- Task history and result tracking
- Custom prompts for automation planning
- Resource management for configurations and data

## Usage Examples

### Using N8N MCP

```python
# Example: Create a workflow automation task
{
  "tool": "n8n_create_workflow",
  "parameters": {
    "workflow_name": "Data Processing Pipeline",
    "nodes": [
      {"type": "webhook", "name": "trigger"},
      {"type": "function", "name": "process_data"},
      {"type": "email", "name": "send_notification"}
    ]
  }
}
```

### Using Figma MCP

```python
# Example: Read design components
{
  "tool": "figma_read_components",
  "parameters": {
    "file_id": "your-figma-file-id",
    "component_type": "buttons"
  }
}
```

### Using Custom Browser Agent MCP

```python
# Example: Create automation task
{
  "tool": "create_automation_task",
  "parameters": {
    "task_name": "Login and Extract Data",
    "url": "https://example.com/login",
    "instructions": "Login with credentials and extract user data",
    "browser_type": "chrome",
    "headless": true
  }
}

# Example: Execute browser action
{
  "tool": "execute_browser_action",
  "parameters": {
    "session_id": "session-123",
    "action_type": "click",
    "selector": "#login-button"
  }
}

# Example: Analyze page content
{
  "tool": "analyze_page_content",
  "parameters": {
    "session_id": "session-123",
    "analysis_type": "extract_text",
    "query": "Find all product information"
  }
}
```

## Claude Desktop Integration

To use these MCP servers with Claude Desktop, add the configuration from `mcp_servers.json` to your Claude Desktop config:

**Location**: `~/.claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "n8n-mcp": {
      "command": "npx",
      "args": ["n8n-mcp"],
      "env": {
        "MCP_MODE": "stdio",
        "LOG_LEVEL": "error",
        "DISABLE_CONSOLE_OUTPUT": "true"
      }
    },
    "cursor-talk-to-figma-mcp": {
      "command": "bunx",
      "args": ["cursor-talk-to-figma-mcp@latest"]
    },
    "brouser-agent-custom-mcp": {
      "command": "python",
      "args": ["/path/to/brouser-agent/mcp_custom_server.py"],
      "env": {
        "BROUSER_AGENT_API_KEY": "your-api-key-here",
        "CUSTOM_MCP_PORT": "8080",
        "LOG_LEVEL": "INFO"
      }
    }
  }
}
```

## Testing the Setup

### 1. Test Custom MCP Server

```bash
# Run the custom server directly
python mcp_custom_server.py

# Test with MCP client
echo '{"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {}}' | python mcp_custom_server.py
```

### 2. Test N8N MCP

```bash
# Test n8n-mcp installation
npx n8n-mcp --help

# Test with environment variables
N8N_API_URL="your-url" N8N_API_KEY="your-key" npx n8n-mcp
```

### 3. Test Figma MCP

```bash
# Test figma-mcp installation
bunx cursor-talk-to-figma-mcp@latest --help

# Test with Figma token
FIGMA_ACCESS_TOKEN="your-token" bunx cursor-talk-to-figma-mcp@latest
```

## Troubleshooting

### Common Issues

1. **MCP SDK Not Found**
   ```bash
   pip install mcp
   ```

2. **Node.js/NPM Issues**
   ```bash
   # Update Node.js and npm
   npm install -g npm@latest
   ```

3. **Bun Not Installed**
   ```bash
   # Install Bun
   curl -fsSL https://bun.sh/install | bash
   ```

4. **Permission Issues**
   ```bash
   chmod +x mcp_custom_server.py
   ```

5. **Environment Variables Not Set**
   - Check that all required environment variables are properly set
   - Use `.env` file for local development

### Debugging

1. **Enable Debug Logging**
   ```bash
   export LOG_LEVEL="DEBUG"
   ```

2. **Check Server Status**
   - Use the `manage_browser_session` tool with action "list"
   - Check the `brouser-agent://config` resource

3. **Validate Configuration**
   - Ensure `mcp_servers.json` is properly formatted
   - Verify all paths are absolute and correct

## Advanced Configuration

### Custom Environment Setup

Create a `.env` file in the project root:

```bash
# N8N Configuration
N8N_API_URL=https://your-n8n-instance.com/api/v1
N8N_API_KEY=your-n8n-api-key

# Figma Configuration
FIGMA_ACCESS_TOKEN=your-figma-access-token
WEBSOCKET_URL=ws://localhost:3001

# Custom MCP Configuration
BROUSER_AGENT_API_KEY=your-api-key
CUSTOM_MCP_PORT=8080
LOG_LEVEL=INFO

# General MCP Settings
MCP_MODE=stdio
DISABLE_CONSOLE_OUTPUT=true
```

### Security Considerations

1. **API Keys**: Never commit API keys to version control
2. **Environment Variables**: Use secure methods to set sensitive variables
3. **Network Access**: Configure firewalls appropriately for MCP servers
4. **Authentication**: Implement proper authentication for production use

## Integration with Browser Agent

The MCP servers integrate seamlessly with Browser Agent's existing features:

- **GUI Integration**: Access MCP tools through the MCP tab
- **Chat Commands**: Use `/mcp` commands to interact with servers
- **Task Logging**: All MCP actions are logged in task history
- **Multi-LLM Support**: MCP tools work with all supported LLMs

## Support and Documentation

- **N8N MCP**: [GitHub Repository](https://github.com/czlonkowski/n8n-mcp)
- **Figma MCP**: [GitHub Repository](https://github.com/sonnylazuardi/cursor-talk-to-figma-mcp)
- **MCP Specification**: [Official Documentation](https://modelcontextprotocol.io/)
- **Browser Agent**: Check the main README.md and MCP_README.md files

For issues specific to the custom implementation, refer to the Browser Agent documentation or create an issue in the project repository.