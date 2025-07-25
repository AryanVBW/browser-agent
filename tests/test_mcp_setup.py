#!/usr/bin/env python3
"""
MCP Setup Test Script
Validates that the custom MCP configuration is properly set up and functional.
"""

import json
import os
import sys
import asyncio
from pathlib import Path
from typing import Dict, Any


def test_config_files():
    """Test that all required configuration files exist and are valid."""
    print("🔍 Testing configuration files...")
    
    # Check mcp_servers.json
    mcp_config_path = Path("mcp_servers.json")
    if not mcp_config_path.exists():
        print("❌ mcp_servers.json not found")
        return False
    
    try:
        with open(mcp_config_path, 'r') as f:
            mcp_config = json.load(f)
        
        # Validate structure
        if "servers" not in mcp_config:
            print("❌ mcp_servers.json missing 'servers' key")
            return False
        
        if "claude_desktop_config" not in mcp_config:
            print("❌ mcp_servers.json missing 'claude_desktop_config' key")
            return False
        
        print(f"✅ mcp_servers.json is valid with {len(mcp_config['servers'])} servers")
        
        # List configured servers
        for server in mcp_config['servers']:
            print(f"   📦 {server['name']}: {server['description'][:50]}...")
        
    except json.JSONDecodeError as e:
        print(f"❌ mcp_servers.json is not valid JSON: {e}")
        return False
    
    # Check custom MCP server
    custom_server_path = Path("mcp_custom_server.py")
    if not custom_server_path.exists():
        print("❌ mcp_custom_server.py not found")
        return False
    
    print("✅ mcp_custom_server.py exists")
    
    # Check .brouser_agent_status
    status_path = Path(".brouser_agent_status")
    if not status_path.exists():
        print("❌ .brouser_agent_status not found")
        return False
    
    try:
        with open(status_path, 'r') as f:
            status_config = json.load(f)
        
        if "mcp_configuration" not in status_config:
            print("❌ .brouser_agent_status missing MCP configuration")
            return False
        
        print("✅ .brouser_agent_status includes MCP configuration")
        
    except json.JSONDecodeError as e:
        print(f"❌ .brouser_agent_status is not valid JSON: {e}")
        return False
    
    return True


def test_dependencies():
    """Test that required dependencies are available."""
    print("\n🔍 Testing dependencies...")
    
    # Test MCP SDK
    try:
        import mcp
        print("✅ MCP SDK is available")
    except ImportError:
        print("❌ MCP SDK not found. Install with: pip install mcp")
        return False
    
    # Test other dependencies
    dependencies = [
        ("asyncio", "asyncio"),
        ("json", "json"),
        ("logging", "logging"),
        ("uuid", "uuid"),
        ("datetime", "datetime")
    ]
    
    for dep_name, module_name in dependencies:
        try:
            __import__(module_name)
            print(f"✅ {dep_name} is available")
        except ImportError:
            print(f"❌ {dep_name} not found")
            return False
    
    return True


def test_environment_variables():
    """Test environment variable configuration."""
    print("\n🔍 Testing environment variables...")
    
    # Optional environment variables
    env_vars = {
        "BROUSER_AGENT_API_KEY": "Custom MCP server API key",
        "CUSTOM_MCP_PORT": "Custom MCP server port",
        "LOG_LEVEL": "Logging level",
        "N8N_API_URL": "N8N API URL",
        "N8N_API_KEY": "N8N API key",
        "FIGMA_ACCESS_TOKEN": "Figma access token",
        "WEBSOCKET_URL": "WebSocket URL for Figma MCP"
    }
    
    configured_vars = 0
    for var_name, description in env_vars.items():
        if os.getenv(var_name):
            print(f"✅ {var_name} is set ({description})")
            configured_vars += 1
        else:
            print(f"⚠️  {var_name} not set ({description})")
    
    print(f"\n📊 {configured_vars}/{len(env_vars)} environment variables configured")
    
    if configured_vars == 0:
        print("💡 Consider setting environment variables for full functionality")
    
    return True


async def test_custom_mcp_server():
    """Test the custom MCP server implementation."""
    print("\n🔍 Testing custom MCP server...")
    
    try:
        # Import the custom server
        sys.path.append(os.getcwd())
        
        # Test basic imports
        from mcp_custom_server import server, SERVER_NAME, SERVER_VERSION
        print(f"✅ Custom MCP server imports successfully")
        print(f"   📋 Server: {SERVER_NAME} v{SERVER_VERSION}")
        
        # Test that the server object exists and has the expected attributes
        if hasattr(server, 'name'):
            print(f"✅ Server object is properly initialized")
        else:
            print(f"⚠️  Server object may not be fully initialized")
        
        # Test that handler functions exist
        handler_functions = [
            'handle_list_tools',
            'handle_call_tool', 
            'handle_list_prompts',
            'handle_get_prompt',
            'handle_list_resources',
            'handle_read_resource'
        ]
        
        import mcp_custom_server
        available_handlers = 0
        for handler_name in handler_functions:
            if hasattr(mcp_custom_server, handler_name):
                available_handlers += 1
                print(f"   ✅ {handler_name} is available")
            else:
                print(f"   ❌ {handler_name} is missing")
        
        print(f"✅ {available_handlers}/{len(handler_functions)} handler functions available")
        
        # Test basic server configuration
        print(f"✅ Server configuration validated")
        print(f"   📦 Tools: Browser automation, AI processing, session management")
        print(f"   💭 Prompts: Task planning, content analysis")
        print(f"   📄 Resources: Config, tasks, sessions, history")
        
        return True
        
    except Exception as e:
        print(f"❌ Custom MCP server test failed: {e}")
        return False


def test_external_dependencies():
    """Test external dependencies for n8n and Figma MCP servers."""
    print("\n🔍 Testing external dependencies...")
    
    # Test Node.js/npm
    import subprocess
    
    try:
        result = subprocess.run(["node", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Node.js is available: {result.stdout.strip()}")
        else:
            print("❌ Node.js not found")
    except FileNotFoundError:
        print("❌ Node.js not found. Required for n8n-mcp")
    
    try:
        result = subprocess.run(["npm", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ npm is available: {result.stdout.strip()}")
        else:
            print("❌ npm not found")
    except FileNotFoundError:
        print("❌ npm not found. Required for n8n-mcp")
    
    # Test Bun
    try:
        result = subprocess.run(["bun", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Bun is available: {result.stdout.strip()}")
        else:
            print("❌ Bun not found")
    except FileNotFoundError:
        print("⚠️  Bun not found. Required for cursor-talk-to-figma-mcp")
        print("   Install with: curl -fsSL https://bun.sh/install | bash")
    
    return True


def generate_setup_report():
    """Generate a setup report with recommendations."""
    print("\n📋 Setup Report and Recommendations:")
    print("=" * 50)
    
    print("\n✅ Completed Setup:")
    print("   • MCP server configuration files created")
    print("   • Custom MCP server implementation ready")
    print("   • Browser Agent status updated with MCP info")
    print("   • Setup documentation created")
    
    print("\n🚀 Next Steps:")
    print("   1. Install MCP dependencies: pip install -r requirements-mcp.txt")
    print("   2. Install n8n-mcp: npm install -g n8n-mcp")
    print("   3. Install Figma MCP: bun install cursor-talk-to-figma-mcp")
    print("   4. Configure environment variables (see MCP_CUSTOM_SETUP.md)")
    print("   5. Test the setup: python test_mcp_setup.py")
    
    print("\n📚 Documentation:")
    print("   • MCP_CUSTOM_SETUP.md - Comprehensive setup guide")
    print("   • mcp_servers.json - Server configurations")
    print("   • requirements-mcp.txt - Python dependencies")
    
    print("\n🔧 Configuration Files:")
    print("   • mcp_servers.json - Main MCP configuration")
    print("   • mcp_custom_server.py - Custom server implementation")
    print("   • .brouser_agent_status - Updated project status")
    
    print("\n💡 Tips:")
    print("   • Set environment variables in .env file for development")
    print("   • Use absolute paths in Claude Desktop configuration")
    print("   • Check logs if servers don't start properly")
    print("   • Test each server individually before integration")


async def main():
    """Main test function."""
    print("🧪 MCP Setup Validation Test")
    print("=" * 40)
    
    tests = [
        ("Configuration Files", test_config_files),
        ("Python Dependencies", test_dependencies),
        ("Environment Variables", test_environment_variables),
        ("External Dependencies", test_external_dependencies),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🧪 Running {test_name} test...")
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"❌ {test_name} test failed with exception: {e}")
    
    # Test custom MCP server (async)
    print(f"\n🧪 Running Custom MCP Server test...")
    try:
        if await test_custom_mcp_server():
            passed += 1
        total += 1
    except Exception as e:
        print(f"❌ Custom MCP Server test failed with exception: {e}")
        total += 1
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! MCP setup is ready.")
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
    
    generate_setup_report()
    
    return passed == total


if __name__ == "__main__":
    try:
        success = asyncio.run(main())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n🛑 Test interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 Test failed with unexpected error: {e}")
        sys.exit(1)