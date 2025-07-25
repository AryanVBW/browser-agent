#!/usr/bin/env python3
"""
Fix CustomTkinter placeholder_text errors

This script identifies and fixes all placeholder_text compatibility issues
in the Browser Agent GUI components.
"""

import re
import os
from pathlib import Path

def analyze_placeholder_issues():
    """Analyze all placeholder_text usage issues"""
    print("🔍 Analyzing placeholder_text Issues")
    print("=" * 40)
    
    gui_files = [
        "brouser_agent/gui/chat_interface.py",
        "brouser_agent/gui/settings_tab.py", 
        "brouser_agent/gui/task_log_tab.py",
        "brouser_agent/gui/brain_tab.py",
        "brouser_agent/gui/browser_tab.py"
    ]
    
    issues = []
    
    for file_path in gui_files:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read()
                lines = content.split('\n')
                
                for i, line in enumerate(lines, 1):
                    if 'placeholder_text=' in line:
                        # Check if it's in a CTkTextbox
                        context_start = max(0, i-5)
                        context_lines = lines[context_start:i+2]
                        context = '\n'.join(context_lines)
                        
                        if 'CTkTextbox' in context:
                            issues.append({
                                'file': file_path,
                                'line': i,
                                'type': 'CTkTextbox',
                                'content': line.strip()
                            })
                        elif 'CTkEntry' in context:
                            issues.append({
                                'file': file_path,
                                'line': i, 
                                'type': 'CTkEntry',
                                'content': line.strip()
                            })
    
    print(f"Found {len(issues)} placeholder_text usages:")
    for issue in issues:
        status = "❌ PROBLEM" if issue['type'] == 'CTkTextbox' else "⚠️ CHECK"
        print(f"  {status} {issue['file']}:{issue['line']} ({issue['type']})")
    
    return issues

def create_placeholder_solution():
    """Create a solution for placeholder text functionality"""
    
    solution_code = '''
"""
CustomTkinter Placeholder Text Solutions

Since CTkTextbox doesn't support placeholder_text natively,
we need alternative approaches.
"""

import customtkinter as ctk

class PlaceholderTextbox(ctk.CTkTextbox):
    """CTkTextbox with placeholder text functionality"""
    
    def __init__(self, master, placeholder_text="", **kwargs):
        # Remove placeholder_text from kwargs to avoid error
        self.placeholder_text = placeholder_text
        if 'placeholder_text' in kwargs:
            del kwargs['placeholder_text']
            
        super().__init__(master, **kwargs)
        
        self.placeholder_color = "#666666"
        self.default_color = self.cget("text_color")
        self.placeholder_active = False
        
        if self.placeholder_text:
            self.show_placeholder()
            self.bind("<FocusIn>", self.on_focus_in)
            self.bind("<FocusOut>", self.on_focus_out)
            self.bind("<KeyPress>", self.on_key_press)
    
    def show_placeholder(self):
        """Show placeholder text"""
        if not self.get("1.0", "end-1c"):
            self.insert("1.0", self.placeholder_text)
            self.configure(text_color=self.placeholder_color)
            self.placeholder_active = True
    
    def hide_placeholder(self):
        """Hide placeholder text"""
        if self.placeholder_active:
            self.delete("1.0", "end")
            self.configure(text_color=self.default_color)
            self.placeholder_active = False
    
    def on_focus_in(self, event):
        """Handle focus in event"""
        self.hide_placeholder()
    
    def on_focus_out(self, event):
        """Handle focus out event"""
        if not self.get("1.0", "end-1c"):
            self.show_placeholder()
    
    def on_key_press(self, event):
        """Handle key press event"""
        if self.placeholder_active:
            self.hide_placeholder()
    
    def get_actual_text(self):
        """Get actual text without placeholder"""
        if self.placeholder_active:
            return ""
        return self.get("1.0", "end-1c")

class SafeCTkEntry(ctk.CTkEntry):
    """CTkEntry with safe placeholder_text handling"""
    
    def __init__(self, master, **kwargs):
        # Check if placeholder_text is supported
        try:
            super().__init__(master, **kwargs)
        except ValueError as e:
            if 'placeholder_text' in str(e):
                # Remove placeholder_text and create without it
                placeholder = kwargs.pop('placeholder_text', '')
                super().__init__(master, **kwargs)
                if placeholder:
                    self.insert(0, placeholder)
                    self.configure(text_color="#666666")
            else:
                raise e
'''
    
    with open("brouser_agent/gui/placeholder_utils.py", "w") as f:
        f.write(solution_code)
    
    print("✅ Created placeholder_utils.py with solutions")

def main():
    """Main fix function"""
    print("🔧 CustomTkinter Placeholder Fix")
    print("=" * 35)
    
    # Analyze issues
    issues = analyze_placeholder_issues()
    
    # Create solution
    create_placeholder_solution()
    
    print(f"\n📋 Next Steps:")
    print("1. Apply fixes to GUI files")
    print("2. Replace CTkTextbox with PlaceholderTextbox where needed")
    print("3. Test the GUI to ensure no more errors")

if __name__ == "__main__":
    main()