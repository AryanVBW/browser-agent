import logging
from typing import Dict, Optional, Any
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import playwright
from playwright.sync_api import sync_playwright

from .detector import BrowserDetector, BrowserInfo


class BrowserManager:
    """Manages browser instances and automation frameworks"""
    
    def __init__(self, headless: bool = False, framework: str = "selenium"):
        self.headless = headless
        self.framework = framework.lower()
        self.detector = BrowserDetector()
        self.available_browsers = self.detector.detect_all()
        self.active_driver = None
        self.playwright_context = None
        self.logger = logging.getLogger(__name__)
        
    def get_available_browsers(self) -> Dict[str, BrowserInfo]:
        """Get all available browsers on the system"""
        return self.available_browsers
    
    def launch_browser(self, browser_name: str = "chrome", **options) -> Any:
        """Launch a browser instance"""
        browser_name = browser_name.lower()
        
        if browser_name not in self.available_browsers:
            raise ValueError(f"Browser {browser_name} not found or not installed")
        
        if not self.available_browsers[browser_name].is_installed:
            raise ValueError(f"Browser {browser_name} is not properly installed")
        
        if self.framework == "selenium":
            return self._launch_selenium_browser(browser_name, **options)
        elif self.framework == "playwright":
            return self._launch_playwright_browser(browser_name, **options)
        else:
            raise ValueError(f"Unsupported framework: {self.framework}")
    
    def _launch_selenium_browser(self, browser_name: str, **options) -> webdriver:
        """Launch browser using Selenium"""
        try:
            if browser_name == "chrome":
                return self._launch_selenium_chrome(**options)
            elif browser_name == "firefox":
                return self._launch_selenium_firefox(**options)
            elif browser_name == "edge":
                return self._launch_selenium_edge(**options)
            else:
                raise ValueError(f"Selenium doesn't support {browser_name}")
        except Exception as e:
            self.logger.error(f"Failed to launch {browser_name} with Selenium: {e}")
            raise
    
    def _launch_selenium_chrome(self, **options) -> webdriver.Chrome:
        """Launch Chrome with Selenium"""
        chrome_options = ChromeOptions()
        
        if self.headless:
            chrome_options.add_argument("--headless=new")
        
        # Default options for better automation
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        
        # Add custom options
        for key, value in options.items():
            if key == "arguments":
                for arg in value:
                    chrome_options.add_argument(arg)
            elif key == "prefs":
                chrome_options.add_experimental_option("prefs", value)
        
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        self.active_driver = driver
        return driver
    
    def _launch_selenium_firefox(self, **options) -> webdriver.Firefox:
        """Launch Firefox with Selenium"""
        firefox_options = FirefoxOptions()
        
        if self.headless:
            firefox_options.add_argument("--headless")
        
        # Default options
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        
        # Add custom options
        for key, value in options.items():
            if key == "arguments":
                for arg in value:
                    firefox_options.add_argument(arg)
            elif key == "prefs":
                for pref_key, pref_value in value.items():
                    firefox_options.set_preference(pref_key, pref_value)
        
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=firefox_options)
        self.active_driver = driver
        return driver
    
    def _launch_selenium_edge(self, **options) -> webdriver.Edge:
        """Launch Edge with Selenium"""
        edge_options = EdgeOptions()
        
        if self.headless:
            edge_options.add_argument("--headless=new")
        
        # Default options
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")
        edge_options.add_argument("--window-size=1920,1080")
        
        # Add custom options
        for key, value in options.items():
            if key == "arguments":
                for arg in value:
                    edge_options.add_argument(arg)
            elif key == "prefs":
                edge_options.add_experimental_option("prefs", value)
        
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=edge_options)
        self.active_driver = driver
        return driver
    
    def _launch_playwright_browser(self, browser_name: str, **options):
        """Launch browser using Playwright"""
        try:
            if not self.playwright_context:
                self.playwright_context = sync_playwright().start()
            
            launch_options = {
                "headless": self.headless,
                **options
            }
            
            if browser_name == "chrome":
                browser = self.playwright_context.chromium.launch(**launch_options)
            elif browser_name == "firefox":
                browser = self.playwright_context.firefox.launch(**launch_options)
            elif browser_name == "edge":
                browser = self.playwright_context.chromium.launch(channel="msedge", **launch_options)
            elif browser_name == "safari":
                browser = self.playwright_context.webkit.launch(**launch_options)
            else:
                raise ValueError(f"Playwright doesn't support {browser_name}")
            
            context = browser.new_context(
                viewport={"width": 1920, "height": 1080},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            )
            page = context.new_page()
            self.active_driver = {"browser": browser, "context": context, "page": page}
            return self.active_driver
            
        except Exception as e:
            self.logger.error(f"Failed to launch {browser_name} with Playwright: {e}")
            raise
    
    def close_browser(self):
        """Close the active browser instance"""
        if self.active_driver:
            try:
                if self.framework == "selenium":
                    self.active_driver.quit()
                elif self.framework == "playwright":
                    if isinstance(self.active_driver, dict):
                        self.active_driver["browser"].close()
                        if self.playwright_context:
                            self.playwright_context.stop()
                            self.playwright_context = None
            except Exception as e:
                self.logger.error(f"Error closing browser: {e}")
            finally:
                self.active_driver = None
    
    def switch_framework(self, framework: str):
        """Switch between automation frameworks"""
        if self.active_driver:
            self.close_browser()
        
        self.framework = framework.lower()
        if self.framework not in ["selenium", "playwright"]:
            raise ValueError(f"Unsupported framework: {framework}")
    
    def get_browser_capabilities(self, browser_name: str) -> Dict[str, Any]:
        """Get capabilities and features of a specific browser"""
        capabilities = {
            "chrome": {
                "supports_extensions": True,
                "supports_mobile_emulation": True,
                "supports_headless": True,
                "supports_screenshots": True,
                "supports_pdf_generation": True
            },
            "firefox": {
                "supports_extensions": True,
                "supports_mobile_emulation": False,
                "supports_headless": True,
                "supports_screenshots": True,
                "supports_pdf_generation": False
            },
            "edge": {
                "supports_extensions": True,
                "supports_mobile_emulation": True,
                "supports_headless": True,
                "supports_screenshots": True,
                "supports_pdf_generation": True
            },
            "safari": {
                "supports_extensions": False,
                "supports_mobile_emulation": False,
                "supports_headless": False,
                "supports_screenshots": True,
                "supports_pdf_generation": False
            }
        }
        
        return capabilities.get(browser_name.lower(), {})
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_browser()