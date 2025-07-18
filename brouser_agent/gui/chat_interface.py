import tkinter as tk
import customtkinter as ctk
import asyncio
import threading
from typing import Dict, Any, Optional
from datetime import datetime
import time
from .placeholder_utils import PlaceholderTextbox


class AnimatedTextWidget(ctk.CTkTextbox):
    """Custom text widget with typing animation"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(state="disabled")
        
    def animate_text(self, text: str, delay: float = 0.03, callback=None):
        """Animate text typing effect"""
        def animate():
            self.configure(state="normal")
            
            for char in text:
                self.insert("end", char)
                self.see("end")
                self.update()
                time.sleep(delay)
            
            if callback:
                callback()
            
            self.configure(state="disabled")
        
        threading.Thread(target=animate, daemon=True).start()
    
    def add_message(self, message: str, sender: str = "user", animate: bool = False):
        """Add a message to the chat"""
        self.configure(state="normal")
        
        # Add timestamp
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Format message based on sender
        if sender == "user":
            prefix = f"[{timestamp}] 👤 You: "
            self.insert("end", prefix, "user_tag")
        elif sender == "ai":
            prefix = f"[{timestamp}] 🤖 Assistant: "
            self.insert("end", prefix, "ai_tag")
        elif sender == "system":
            prefix = f"[{timestamp}] ⚙️ System: "
            self.insert("end", prefix, "system_tag")
        
        # Add the message
        if animate and sender == "ai":
            self.configure(state="disabled")
            self.animate_text(message + "\n\n")
        else:
            self.insert("end", message + "\n\n")
            self.configure(state="disabled")
        
        self.see("end")


class ChatInterface:
    """Main chat interface for interacting with the AI agent"""
    
    def __init__(self, parent, main_window):
        self.parent = parent
        self.main_window = main_window
        self.is_processing = False
        
        self.create_widgets()
        self.setup_layout()
        self.setup_tags()
        
        # Welcome message
        self.add_welcome_message()
    
    def create_widgets(self):
        """Create chat interface widgets"""
        # Main chat container
        self.chat_container = ctk.CTkFrame(self.parent)
        
        # Chat display area
        self.chat_frame = ctk.CTkFrame(self.chat_container)
        
        # Chat text area with scrollbar
        self.chat_display = AnimatedTextWidget(
            self.chat_frame,
            height=400,
            font=ctk.CTkFont(size=12),
            wrap="word"
        )
        
        # Scrollbar for chat
        self.chat_scrollbar = ctk.CTkScrollbar(
            self.chat_frame,
            command=self.chat_display.yview
        )
        self.chat_display.configure(yscrollcommand=self.chat_scrollbar.set)
        
        # Input area
        self.input_frame = ctk.CTkFrame(self.chat_container)
        
        # Input text area
        self.input_text = PlaceholderTextbox(
            self.input_frame,
            height=80,
            font=ctk.CTkFont(size=12),
            placeholder_text="Type your request here... (e.g., 'Search for Python tutorials on YouTube')"
        )
        
        # Button frame
        self.button_frame = ctk.CTkFrame(self.input_frame, fg_color="transparent")
        
        # Send button
        self.send_button = ctk.CTkButton(
            self.button_frame,
            text="🚀 Send",
            command=self.send_message,
            font=ctk.CTkFont(size=12, weight="bold"),
            height=35
        )
        
        # Clear button
        self.clear_button = ctk.CTkButton(
            self.button_frame,
            text="🗑️ Clear",
            command=self.clear_chat,
            font=ctk.CTkFont(size=12),
            height=35,
            fg_color="#666666",
            hover_color="#777777"
        )
        
        # Stop button (shown during processing)
        self.stop_button = ctk.CTkButton(
            self.button_frame,
            text="⏹️ Stop",
            command=self.stop_processing,
            font=ctk.CTkFont(size=12),
            height=35,
            fg_color="#e74c3c",
            hover_color="#c0392b"
        )
        
        # Quick actions frame
        self.quick_actions_frame = ctk.CTkFrame(self.chat_container)
        self.create_quick_actions()
        
        # Status indicator
        self.status_frame = ctk.CTkFrame(self.input_frame, fg_color="transparent")
        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="💡 Ready to help with web automation tasks",
            font=ctk.CTkFont(size=11),
            text_color="#888888"
        )
        
        # Typing indicator
        self.typing_indicator = ctk.CTkLabel(
            self.status_frame,
            text="🤖 AI is thinking...",
            font=ctk.CTkFont(size=11),
            text_color="#4CAF50"
        )
    
    def create_quick_actions(self):
        """Create quick action buttons"""
        quick_actions_label = ctk.CTkLabel(
            self.quick_actions_frame,
            text="💡 Quick Actions:",
            font=ctk.CTkFont(size=12, weight="bold")
        )
        quick_actions_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        # Quick action buttons
        actions = [
            ("🔍 Search Google", "Search Google for 'latest AI news'"),
            ("📧 Open Gmail", "Go to Gmail and check for new emails"),
            ("🛒 Amazon Search", "Go to Amazon and search for 'wireless headphones'"),
            ("📰 Check News", "Go to BBC News and show me the top headlines"),
            ("🌡️ Weather Check", "Check the weather forecast for today"),
            ("💰 Stock Prices", "Check the current stock price of Apple")
        ]
        
        # Create buttons in rows
        for i in range(0, len(actions), 3):
            row_frame = ctk.CTkFrame(self.quick_actions_frame, fg_color="transparent")
            row_frame.pack(fill="x", padx=10, pady=2)
            
            for j in range(3):
                if i + j < len(actions):
                    action_text, action_prompt = actions[i + j]
                    btn = ctk.CTkButton(
                        row_frame,
                        text=action_text,
                        command=lambda p=action_prompt: self.send_quick_action(p),
                        font=ctk.CTkFont(size=10),
                        height=30,
                        width=150
                    )
                    btn.pack(side="left", padx=5, pady=2)
    
    def setup_layout(self):
        """Setup the layout of chat interface"""
        self.chat_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Chat display area
        self.chat_frame.pack(fill="both", expand=True, pady=(0, 10))
        self.chat_display.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)
        self.chat_scrollbar.pack(side="right", fill="y", padx=(0, 10), pady=10)
        
        # Quick actions
        self.quick_actions_frame.pack(fill="x", pady=(0, 10))
        
        # Input area
        self.input_frame.pack(fill="x")
        self.input_text.pack(fill="x", padx=10, pady=(10, 5))
        
        # Status
        self.status_frame.pack(fill="x", padx=10)
        self.status_label.pack(side="left")
        
        # Buttons
        self.button_frame.pack(fill="x", padx=10, pady=(5, 10))
        self.send_button.pack(side="right", padx=(5, 0))
        self.clear_button.pack(side="right", padx=(5, 5))
        
        # Hide typing indicator and stop button initially
        self.hide_typing_indicator()
        self.hide_stop_button()
        
        # Bind Enter key
        self.input_text.bind("<Control-Return>", lambda e: self.send_message())
    
    def setup_tags(self):
        """Setup text tags for different message types"""
        self.chat_display.tag_config("user_tag", foreground="#4CAF50")
        self.chat_display.tag_config("ai_tag", foreground="#2196F3")
        self.chat_display.tag_config("system_tag", foreground="#FF9800")
    
    def add_welcome_message(self):
        """Add welcome message to chat"""
        welcome_text = """Welcome to Browser Agent! 🎉

I'm your AI-powered web automation assistant. I can help you with:

🔍 Web browsing and searching
📝 Filling out forms automatically
🛒 E-commerce tasks (searching, comparing prices)
📧 Email management
📊 Data extraction from websites
🔗 Navigating complex web applications

Just tell me what you'd like me to do in natural language, and I'll break it down into steps and execute them for you!

Try asking me something like:
• "Search for Python programming tutorials on YouTube"
• "Go to Amazon and find the best-rated wireless headphones under $100"
• "Fill out a contact form with my information"
• "Compare flight prices from NYC to LA"

What would you like me to help you with today?"""
        
        self.chat_display.add_message(welcome_text, "ai", animate=True)
    
    def send_message(self):
        """Send user message and process with AI"""
        if self.is_processing:
            return
        
        user_input = self.input_text.get_actual_text().strip()
        if not user_input:
            return
        
        # Add user message to chat
        self.chat_display.add_message(user_input, "user")
        
        # Clear input
        self.input_text.set_text("")
        
        # Process message
        self.process_user_message(user_input)
    
    def send_quick_action(self, prompt: str):
        """Send a quick action prompt"""
        if self.is_processing:
            return
        
        # Set text in input area
        self.input_text.set_text(prompt)
        
        # Send the message
        self.send_message()
    
    def process_user_message(self, message: str):
        """Process user message with AI agent"""
        def process_worker():
            try:
                self.set_processing_state(True)
                
                # Check if this is a task execution request or just conversation
                if self.is_task_request(message):
                    # Execute as browser automation task
                    self.root_after(0, lambda: self.chat_display.add_message(
                        "I'll help you with that task. Let me analyze what needs to be done...", "ai", True
                    ))
                    
                    # Execute the task
                    result = asyncio.run(self.execute_browser_task(message))
                    
                    if result:
                        if result.success:
                            response = f"✅ Task completed successfully!\n\n"
                            response += f"⏱️ Execution time: {result.execution_time:.2f} seconds\n"
                            response += f"📝 Steps executed: {len(result.step_results)}\n"
                            
                            if result.screenshots:
                                response += f"📸 Screenshots saved: {len(result.screenshots)}\n"
                                for screenshot in result.screenshots:
                                    response += f"   • {screenshot}\n"
                        else:
                            response = f"❌ Task failed: {result.error_message}\n\n"
                            response += "Let me know if you'd like me to try a different approach!"
                    else:
                        response = "I encountered an issue while processing your request. Please check that the browser agent is properly configured."
                else:
                    # Generate conversational response
                    response = asyncio.run(self.generate_ai_response(message))
                
                # Add AI response to chat
                self.root_after(0, lambda: self.chat_display.add_message(response, "ai", True))
                
                # Add to task history
                task_data = {
                    'user_prompt': message,
                    'ai_response': response,
                    'execution_result': result if 'result' in locals() else None,
                    'status': 'completed'
                }
                self.root_after(0, lambda: self.main_window.add_task_to_history(task_data))
                
            except Exception as e:
                error_response = f"I apologize, but I encountered an error: {str(e)}\n\nPlease try again or check your configuration."
                self.root_after(0, lambda: self.chat_display.add_message(error_response, "ai"))
            finally:
                self.root_after(0, lambda: self.set_processing_state(False))
        
        threading.Thread(target=process_worker, daemon=True).start()
    
    def is_task_request(self, message: str) -> bool:
        """Determine if message is a task execution request"""
        task_keywords = [
            'go to', 'navigate', 'search', 'click', 'fill', 'submit', 'download',
            'book', 'buy', 'purchase', 'find', 'extract', 'scrape', 'automate',
            'open', 'close', 'scroll', 'select', 'type', 'enter', 'compare'
        ]
        
        message_lower = message.lower()
        return any(keyword in message_lower for keyword in task_keywords)
    
    async def execute_browser_task(self, prompt: str):
        """Execute browser automation task"""
        try:
            if self.main_window.agent:
                return await self.main_window.agent.execute_task(prompt)
            else:
                raise Exception("Browser agent not initialized")
        except Exception as e:
            print(f"Error executing task: {e}")
            return None
    
    async def generate_ai_response(self, message: str) -> str:
        """Generate conversational AI response"""
        try:
            if self.main_window.llm_processor:
                return await self.main_window.llm_processor.generate_response(message)
            else:
                return "I'm still initializing my AI capabilities. Please wait a moment and try again."
        except Exception as e:
            return f"I encountered an error while processing your message: {str(e)}"
    
    def set_processing_state(self, processing: bool):
        """Set the processing state and update UI"""
        self.is_processing = processing
        
        if processing:
            self.show_typing_indicator()
            self.show_stop_button()
            self.send_button.configure(state="disabled")
            self.main_window.update_status("Processing request...", 0.5)
        else:
            self.hide_typing_indicator()
            self.hide_stop_button()
            self.send_button.configure(state="normal")
            self.main_window.update_status("Ready", 0)
    
    def show_typing_indicator(self):
        """Show typing indicator"""
        self.status_label.pack_forget()
        self.typing_indicator.pack(side="left")
        
        # Animate typing indicator
        self.animate_typing_indicator()
    
    def hide_typing_indicator(self):
        """Hide typing indicator"""
        self.typing_indicator.pack_forget()
        self.status_label.pack(side="left")
    
    def show_stop_button(self):
        """Show stop button"""
        self.stop_button.pack(side="right", padx=(5, 5))
    
    def hide_stop_button(self):
        """Hide stop button"""
        self.stop_button.pack_forget()
    
    def animate_typing_indicator(self):
        """Animate the typing indicator dots"""
        if self.is_processing:
            current_text = self.typing_indicator.cget("text")
            if current_text.endswith("..."):
                self.typing_indicator.configure(text="🤖 AI is thinking")
            else:
                self.typing_indicator.configure(text=current_text + ".")
            
            # Schedule next animation
            self.parent.after(500, self.animate_typing_indicator)
    
    def stop_processing(self):
        """Stop current processing"""
        self.set_processing_state(False)
        self.chat_display.add_message("Processing stopped by user.", "system")
    
    def clear_chat(self):
        """Clear the chat display"""
        self.chat_display.configure(state="normal")
        self.chat_display.delete("1.0", "end")
        self.chat_display.configure(state="disabled")
        
        # Add welcome message back
        self.add_welcome_message()
    
    def root_after(self, delay, callback):
        """Safe way to schedule GUI updates from background thread"""
        try:
            self.parent.after(delay, callback)
        except:
            pass