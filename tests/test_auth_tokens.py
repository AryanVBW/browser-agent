#!/usr/bin/env python3
"""
Test script to demonstrate MCP server authentication token functionality
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from brouser_agent.mcp.types import MCPServer
from brouser_agent.mcp.server_manager import MCPServerManager

def test_auth_token_detection():
    """Test that servers requiring auth tokens are properly detected"""
    print("Testing MCP Server Authentication Token Detection")
    print("=" * 50)
    
    # Create a test server manager
    server_manager = MCPServerManager()
    
    # Test servers that require authentication
    test_servers = [
        {
            "name": "brave-search",
            "expected_tokens": ["BRAVE_API_KEY"]
        },
        {
            "name": "github", 
            "expected_tokens": ["GITHUB_PERSONAL_ACCESS_TOKEN"]
        },
        {
            "name": "postgres",
            "expected_tokens": ["POSTGRES_CONNECTION_STRING"]
        }
    ]
    
    for test_case in test_servers:
        server_name = test_case["name"]
        expected_tokens = test_case["expected_tokens"]
        
        server = server_manager.get_server(server_name)
        if server:
            print(f"\n📦 Server: {server_name}")
            print(f"   Description: {server.description}")
            
            if server.env:
                print(f"   Environment Variables:")
                missing_tokens = []
                
                for key, value in server.env.items():
                    status = "✅ SET" if value else "❌ MISSING"
                    print(f"     - {key}: {status}")
                    
                    # Check if this is a token that needs to be prompted for
                    if not value and any(token_keyword in key.lower() for token_keyword in ['api_key', 'token', 'key', 'secret', 'password', 'connection']):
                        missing_tokens.append(key)
                
                if missing_tokens:
                    print(f"   🔐 Authentication Required: {', '.join(missing_tokens)}")
                else:
                    print(f"   ✅ All tokens configured")
            else:
                print(f"   ℹ️  No authentication required")
        else:
            print(f"\n❌ Server '{server_name}' not found")
    
    print("\n" + "=" * 50)
    print("✅ Authentication token detection test completed!")
    print("\nTo test the GUI functionality:")
    print("1. Run: python run_gui.py")
    print("2. Go to the MCP tab")
    print("3. Try enabling a server that requires authentication")
    print("4. You should see a dialog prompting for API tokens")

if __name__ == "__main__":
    test_auth_token_detection()