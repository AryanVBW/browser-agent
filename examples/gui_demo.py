#!/usr/bin/env python3
"""
GUI Demo for Browser Agent

This script demonstrates the full GUI functionality including:
- Multi-LLM brain configuration (OpenAI, Claude, Gemini)
- Interactive chat interface with animations
- Browser control and automation
- Task logging and history
- Settings management
"""

import os
import sys

# Add the brouser_agent directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from brouser_agent.gui.main_window import main

if __name__ == "__main__":
    print("""
🤖 Browser Agent GUI Demo
========================

This demo showcases the complete Browser Agent GUI with:

🧠 Multi-LLM Support:
   • OpenAI (GPT-3.5, GPT-4, GPT-4 Turbo)
   • Claude (Opus, Sonnet, Haiku)
   • Gemini (Pro, Pro Vision)

💬 Interactive Chat:
   • Natural language task requests
   • Animated typing responses
   • Quick action buttons
   • Real-time status updates

🌐 Browser Control:
   • Automatic browser detection
   • Manual and automated control
   • Live automation logs
   • Screenshot capabilities

📜 Task Management:
   • Complete task history
   • Filtering and search
   • Performance statistics
   • Export capabilities

⚙️ Settings:
   • Comprehensive configuration
   • Theme customization
   • Security settings
   • Performance tuning

Prerequisites:
1. Set environment variables for AI providers:
   export OPENAI_API_KEY="your-openai-key"
   export CLAUDE_API_KEY="your-claude-key"
   export GEMINI_API_KEY="your-gemini-key"

2. Ensure browsers are installed (Chrome, Firefox, etc.)

3. Install dependencies:
   pip install -r requirements.txt

Starting GUI...
""")
    
    main()