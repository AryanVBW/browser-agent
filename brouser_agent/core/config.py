import os
from typing import Optional, Dict, Any
from dataclasses import dataclass, field
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    """Configuration settings for the browser agent"""
    
    # AI Settings
    openai_api_key: Optional[str] = field(default_factory=lambda: os.getenv("OPENAI_API_KEY"))
    claude_api_key: Optional[str] = field(default_factory=lambda: os.getenv("CLAUDE_API_KEY"))
    gemini_api_key: Optional[str] = field(default_factory=lambda: os.getenv("GEMINI_API_KEY"))
    ai_model: str = "gpt-3.5-turbo"
    ai_provider: str = "openai"  # openai, claude, gemini
    max_tokens: int = 2000
    temperature: float = 0.1
    
    # Browser Settings
    default_browser: str = "chrome"
    headless: bool = False
    automation_framework: str = "selenium"  # selenium or playwright
    page_load_timeout: int = 30
    implicit_wait: int = 10
    
    # Window Settings
    window_width: int = 1920
    window_height: int = 1080
    
    # Behavior Settings
    screenshot_on_error: bool = True
    auto_scroll: bool = True
    human_like_delays: bool = True
    min_delay: float = 0.5
    max_delay: float = 2.0
    
    # Security Settings
    allow_file_downloads: bool = False
    allow_notifications: bool = False
    allow_location: bool = False
    allow_microphone: bool = False
    allow_camera: bool = False
    
    # Logging Settings
    log_level: str = "INFO"
    log_file: Optional[str] = None
    
    # Plugin Settings
    plugins_enabled: bool = True
    plugin_directory: str = "plugins"
    
    # Container Settings
    use_container: bool = False
    container_image: str = "selenium/standalone-chrome:latest"
    
    def validate(self) -> bool:
        """Validate configuration settings"""
        # Check that at least one AI provider is configured
        if not any([self.openai_api_key, self.claude_api_key, self.gemini_api_key]):
            raise ValueError("At least one AI provider API key is required (OpenAI, Claude, or Gemini)")
        
        if self.automation_framework not in ["selenium", "playwright"]:
            raise ValueError("automation_framework must be 'selenium' or 'playwright'")
        
        if self.ai_provider not in ["openai", "claude", "gemini"]:
            raise ValueError("ai_provider must be 'openai', 'claude', or 'gemini'")
        
        return True
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'Config':
        """Create config from dictionary"""
        return cls(**{k: v for k, v in config_dict.items() if hasattr(cls, k)})
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert config to dictionary"""
        return {
            field.name: getattr(self, field.name)
            for field in self.__dataclass_fields__.values()
        }