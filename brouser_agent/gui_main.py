#!/usr/bin/env python3
"""
Main entry point for Browser Agent GUI
"""

import sys
import os
import traceback

# Add current directory to path to ensure imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from gui.main_window import MainWindow
except ImportError as e:
    print(f"Import error: {e}")
    print("Please ensure all dependencies are installed: pip install -r requirements.txt")
    sys.exit(1)


def main():
    """Main entry point"""
    try:
        print("🤖 Starting Browser Agent GUI...")
        
        # Create and run the main window
        app = MainWindow()
        app.run()
        
    except KeyboardInterrupt:
        print("\n👋 Browser Agent GUI closed by user")
    except Exception as e:
        print(f"❌ Fatal error starting Browser Agent GUI: {e}")
        print("\nFull error traceback:")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()