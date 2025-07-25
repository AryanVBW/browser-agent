# MCP Server Authentication Token Feature

## Overview

The MCP (Model Context Protocol) integration now includes automatic detection and prompting for authentication tokens when enabling servers that require them.

## How It Works

### Automatic Detection
When you try to enable an MCP server, the system automatically:
1. Checks if the server has environment variables configured
2. Identifies variables that likely contain authentication tokens (API keys, tokens, secrets, etc.)
3. Prompts you to enter missing tokens before enabling the server

### Supported Token Types
The system detects environment variables containing these keywords:
- `api_key`
- `token` 
- `key`
- `secret`
- `password`
- `connection`

### Servers That Require Authentication

#### Brave Search
- **Required**: `BRAVE_API_KEY`
- **How to get**: Visit https://api.search.brave.com/app/keys

#### GitHub
- **Required**: `GITHUB_PERSONAL_ACCESS_TOKEN`
- **How to get**: GitHub Settings > Developer settings > Personal access tokens

#### PostgreSQL
- **Required**: `POSTGRES_CONNECTION_STRING`
- **Format**: `postgresql://username:password@host:port/database`

## User Experience

### First-Time Setup
1. Go to the MCP tab in the GUI
2. Find a server that requires authentication (marked with 🔐)
3. Click "▶️ Enable"
4. A dialog will appear requesting the required tokens
5. Enter your tokens and click "Save & Enable"

### Managing Existing Tokens
1. For servers with environment variables, you'll see a "⚙️ Config" button
2. Click it to update or modify authentication tokens
3. Changes are saved immediately and applied on next connection

## Security Features

- **Masked Input**: Sensitive fields (secrets, passwords) are automatically masked with asterisks
- **Local Storage**: Tokens are stored locally in your MCP configuration files
- **No Transmission**: Tokens are never sent to external services except the intended MCP server

## Testing

Run the test script to verify token detection:
```bash
python test_auth_tokens.py
```

This will show which servers require authentication and their current token status.

## Troubleshooting

### Server Won't Connect After Adding Tokens
1. Check that the token is valid and has the required permissions
2. Verify the token format matches the server's requirements
3. Try disabling and re-enabling the server
4. Check the console logs for specific error messages

### Token Dialog Doesn't Appear
1. Ensure the server has environment variables configured
2. Check that the environment variable names contain recognized keywords
3. Verify the server is properly installed

## Future Enhancements

- Support for OAuth flows
- Token validation before saving
- Encrypted token storage
- Bulk token management
- Integration with system keychain/credential managers