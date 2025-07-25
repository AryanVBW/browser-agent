// Browser Agent Documentation Website - Main JavaScript

// Global state
const state = {
    searchIndex: [],
    isSearchLoaded: false,
    isMobileMenuOpen: false,
    currentTheme: 'auto'
};

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    // Initialize all components
    initializeNavigation();
    initializeSearch();
    initializeAnimations();
    initializeTheme();
    initializeMobileMenu();
    initializeScrollEffects();
    initializeLazyLoading();
    
    // Load search index
    loadSearchIndex();
    
    console.log('Browser Agent Documentation initialized');
}

// Navigation functionality
function initializeNavigation() {
    const navbar = document.querySelector('.navbar');
    const navLinks = document.querySelectorAll('.nav-link');
    
    // Smooth scrolling for anchor links
    navLinks.forEach(link => {
        if (link.getAttribute('href').startsWith('#')) {
            link.addEventListener('click', function(e) {
                e.preventDefault();
                const targetId = this.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);
                
                if (targetElement) {
                    const offsetTop = targetElement.offsetTop - 80; // Account for fixed navbar
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            });
        }
    });
    
    // Navbar scroll effect
    let lastScrollY = window.scrollY;
    
    window.addEventListener('scroll', function() {
        const currentScrollY = window.scrollY;
        
        if (currentScrollY > 100) {
            navbar.style.background = 'rgba(255, 255, 255, 0.98)';
            navbar.style.backdropFilter = 'blur(20px)';
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.backdropFilter = 'blur(10px)';
        }
        
        // Hide/show navbar on scroll
        if (currentScrollY > lastScrollY && currentScrollY > 200) {
            navbar.style.transform = 'translateY(-100%)';
        } else {
            navbar.style.transform = 'translateY(0)';
        }
        
        lastScrollY = currentScrollY;
    });
}

// Search functionality
function initializeSearch() {
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');
    
    if (!searchInput || !searchResults) return;
    
    let searchTimeout;
    
    searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        const query = this.value.trim();
        
        if (query.length < 2) {
            hideSearchResults();
            return;
        }
        
        searchTimeout = setTimeout(() => {
            performSearch(query);
        }, 300);
    });
    
    searchInput.addEventListener('focus', function() {
        if (this.value.trim().length >= 2) {
            showSearchResults();
        }
    });
    
    // Hide search results when clicking outside
    document.addEventListener('click', function(e) {
        if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
            hideSearchResults();
        }
    });
    
    // Keyboard navigation for search results
    searchInput.addEventListener('keydown', function(e) {
        const results = searchResults.querySelectorAll('.search-result');
        const activeResult = searchResults.querySelector('.search-result.active');
        
        if (e.key === 'ArrowDown') {
            e.preventDefault();
            if (activeResult) {
                activeResult.classList.remove('active');
                const next = activeResult.nextElementSibling;
                if (next) {
                    next.classList.add('active');
                } else {
                    results[0]?.classList.add('active');
                }
            } else {
                results[0]?.classList.add('active');
            }
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            if (activeResult) {
                activeResult.classList.remove('active');
                const prev = activeResult.previousElementSibling;
                if (prev) {
                    prev.classList.add('active');
                } else {
                    results[results.length - 1]?.classList.add('active');
                }
            } else {
                results[results.length - 1]?.classList.add('active');
            }
        } else if (e.key === 'Enter') {
            e.preventDefault();
            const activeResult = searchResults.querySelector('.search-result.active');
            if (activeResult) {
                const link = activeResult.querySelector('a');
                if (link) {
                    window.location.href = link.href;
                }
            }
        } else if (e.key === 'Escape') {
            hideSearchResults();
            searchInput.blur();
        }
    });
}

function loadSearchIndex() {
    // Create a simple search index from page content
    const searchableContent = [
        {
            title: 'Quick Start Guide',
            description: 'Get up and running with Browser Agent in minutes',
            url: './pages/quick-start.html',
            keywords: ['quick', 'start', 'getting started', 'installation', 'setup']
        },
        {
            title: 'Installation & Setup',
            description: 'Complete installation guide for all platforms',
            url: './pages/installation.html',
            keywords: ['install', 'setup', 'docker', 'pip', 'requirements']
        },
        {
            title: 'Features & Use Cases',
            description: 'Explore all features and real-world automation scenarios',
            url: './pages/features.html',
            keywords: ['features', 'automation', 'browser', 'ai', 'multi-browser']
        },
        {
            title: 'MCP Integration',
            description: 'Model Context Protocol integration and external tools',
            url: './pages/mcp-integration.html',
            keywords: ['mcp', 'model context protocol', 'integration', 'tools', 'plugins']
        },
        {
            title: 'API Reference',
            description: 'Complete API documentation and plugin development',
            url: './pages/api.html',
            keywords: ['api', 'reference', 'documentation', 'plugins', 'development']
        },
        {
            title: 'Troubleshooting',
            description: 'Common issues, debugging tips, and solutions',
            url: './pages/troubleshooting.html',
            keywords: ['troubleshooting', 'debug', 'issues', 'problems', 'solutions']
        },
        {
            title: 'Browser Automation',
            description: 'AI-powered web automation with multi-browser support',
            url: '#overview',
            keywords: ['browser', 'automation', 'selenium', 'playwright', 'web scraping']
        },
        {
            title: 'AI Integration',
            description: 'OpenAI GPT, Claude, and Gemini model integration',
            url: './pages/ai-integration.html',
            keywords: ['ai', 'openai', 'claude', 'gemini', 'llm', 'natural language']
        }
    ];
    
    state.searchIndex = searchableContent;
    state.isSearchLoaded = true;
}

function performSearch(query) {
    if (!state.isSearchLoaded) {
        return;
    }
    
    const results = state.searchIndex.filter(item => {
        const searchText = `${item.title} ${item.description} ${item.keywords.join(' ')}`.toLowerCase();
        return searchText.includes(query.toLowerCase());
    });
    
    displaySearchResults(results, query);
}

function displaySearchResults(results, query) {
    const searchResults = document.getElementById('search-results');
    
    if (results.length === 0) {
        searchResults.innerHTML = `
            <div class="search-no-results">
                <p>No results found for "${query}"</p>
            </div>
        `;
    } else {
        searchResults.innerHTML = results.map(result => `
            <div class="search-result">
                <a href="${result.url}">
                    <h4>${highlightText(result.title, query)}</h4>
                    <p>${highlightText(result.description, query)}</p>
                </a>
            </div>
        `).join('');
    }
    
    showSearchResults();
}

function highlightText(text, query) {
    const regex = new RegExp(`(${query})`, 'gi');
    return text.replace(regex, '<mark>$1</mark>');
}

function showSearchResults() {
    const searchResults = document.getElementById('search-results');
    searchResults.style.display = 'block';
}

function hideSearchResults() {
    const searchResults = document.getElementById('search-results');
    searchResults.style.display = 'none';
}

// Animation functionality
function initializeAnimations() {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animateElements = document.querySelectorAll('.feature-card, .doc-card, .install-option');
    animateElements.forEach(el => {
        el.classList.add('animate-on-scroll');
        observer.observe(el);
    });
    
    // Add CSS for animations
    const style = document.createElement('style');
    style.textContent = `
        .animate-on-scroll {
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.6s ease, transform 0.6s ease;
        }
        
        .animate-on-scroll.animate-in {
            opacity: 1;
            transform: translateY(0);
        }
        
        .search-result {
            padding: 12px 16px;
            border-bottom: 1px solid var(--gray-200);
            transition: background-color 0.2s ease;
        }
        
        .search-result:hover,
        .search-result.active {
            background-color: var(--gray-50);
        }
        
        .search-result a {
            display: block;
            text-decoration: none;
            color: inherit;
        }
        
        .search-result h4 {
            font-size: 14px;
            font-weight: 600;
            margin: 0 0 4px 0;
            color: var(--text-primary);
        }
        
        .search-result p {
            font-size: 12px;
            margin: 0;
            color: var(--text-secondary);
        }
        
        .search-no-results {
            padding: 16px;
            text-align: center;
            color: var(--text-secondary);
            font-size: 14px;
        }
        
        .search-result mark {
            background-color: var(--primary-color);
            color: white;
            padding: 1px 2px;
            border-radius: 2px;
        }
    `;
    document.head.appendChild(style);
}

// Theme functionality
function initializeTheme() {
    const savedTheme = localStorage.getItem('browser-agent-theme') || 'auto';
    state.currentTheme = savedTheme;
    applyTheme(savedTheme);
    
    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
        if (state.currentTheme === 'auto') {
            applyTheme('auto');
        }
    });
}

function applyTheme(theme) {
    const html = document.documentElement;
    
    if (theme === 'dark') {
        html.classList.add('dark-theme');
    } else if (theme === 'light') {
        html.classList.remove('dark-theme');
    } else {
        // Auto theme
        if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
            html.classList.add('dark-theme');
        } else {
            html.classList.remove('dark-theme');
        }
    }
}

function toggleTheme() {
    const themes = ['light', 'dark', 'auto'];
    const currentIndex = themes.indexOf(state.currentTheme);
    const nextTheme = themes[(currentIndex + 1) % themes.length];
    
    state.currentTheme = nextTheme;
    localStorage.setItem('browser-agent-theme', nextTheme);
    applyTheme(nextTheme);
}

// Mobile menu functionality
function initializeMobileMenu() {
    const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (!mobileMenuToggle || !navMenu) return;
    
    mobileMenuToggle.addEventListener('click', function() {
        state.isMobileMenuOpen = !state.isMobileMenuOpen;
        
        if (state.isMobileMenuOpen) {
            navMenu.classList.add('mobile-menu-open');
            mobileMenuToggle.classList.add('active');
            document.body.style.overflow = 'hidden';
        } else {
            navMenu.classList.remove('mobile-menu-open');
            mobileMenuToggle.classList.remove('active');
            document.body.style.overflow = '';
        }
    });
    
    // Close mobile menu when clicking on a link
    const navLinks = navMenu.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (state.isMobileMenuOpen) {
                navMenu.classList.remove('mobile-menu-open');
                mobileMenuToggle.classList.remove('active');
                document.body.style.overflow = '';
                state.isMobileMenuOpen = false;
            }
        });
    });
    
    // Add mobile menu styles
    const mobileStyle = document.createElement('style');
    mobileStyle.textContent = `
        @media (max-width: 768px) {
            .nav-menu {
                position: fixed;
                top: 70px;
                left: 0;
                right: 0;
                background: var(--bg-primary);
                border-top: 1px solid var(--gray-200);
                padding: var(--space-6);
                flex-direction: column;
                gap: var(--space-4);
                transform: translateY(-100%);
                opacity: 0;
                visibility: hidden;
                transition: all 0.3s ease;
                z-index: var(--z-dropdown);
                box-shadow: var(--shadow-lg);
            }
            
            .nav-menu.mobile-menu-open {
                display: flex;
                transform: translateY(0);
                opacity: 1;
                visibility: visible;
            }
            
            .mobile-menu-toggle.active span:nth-child(1) {
                transform: rotate(45deg) translate(5px, 5px);
            }
            
            .mobile-menu-toggle.active span:nth-child(2) {
                opacity: 0;
            }
            
            .mobile-menu-toggle.active span:nth-child(3) {
                transform: rotate(-45deg) translate(7px, -6px);
            }
        }
    `;
    document.head.appendChild(mobileStyle);
}

// Scroll effects
function initializeScrollEffects() {
    // Parallax effect for hero section
    const hero = document.querySelector('.hero');
    const heroVisual = document.querySelector('.hero-visual');
    
    if (hero && heroVisual) {
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const rate = scrolled * -0.5;
            
            if (scrolled < hero.offsetHeight) {
                heroVisual.style.transform = `translateY(${rate}px)`;
            }
        });
    }
    
    // Progress indicator
    createProgressIndicator();
}

function createProgressIndicator() {
    const progressBar = document.createElement('div');
    progressBar.className = 'scroll-progress';
    progressBar.innerHTML = '<div class="scroll-progress-bar"></div>';
    document.body.appendChild(progressBar);
    
    const progressBarFill = progressBar.querySelector('.scroll-progress-bar');
    
    window.addEventListener('scroll', () => {
        const scrollTop = window.pageYOffset;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrollPercent = (scrollTop / docHeight) * 100;
        
        progressBarFill.style.width = `${scrollPercent}%`;
    });
    
    // Add progress bar styles
    const progressStyle = document.createElement('style');
    progressStyle.textContent = `
        .scroll-progress {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background: rgba(0, 0, 0, 0.1);
            z-index: var(--z-fixed);
        }
        
        .scroll-progress-bar {
            height: 100%;
            background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
            width: 0%;
            transition: width 0.1s ease;
        }
    `;
    document.head.appendChild(progressStyle);
}

// Lazy loading
function initializeLazyLoading() {
    const lazyImages = document.querySelectorAll('img[data-src]');
    
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        lazyImages.forEach(img => {
            img.classList.add('lazy');
            imageObserver.observe(img);
        });
    } else {
        // Fallback for browsers without IntersectionObserver
        lazyImages.forEach(img => {
            img.src = img.dataset.src;
        });
    }
}

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Analytics and tracking (placeholder)
function trackEvent(eventName, properties = {}) {
    // Implement analytics tracking here
    console.log('Event tracked:', eventName, properties);
}

// Error handling
window.addEventListener('error', function(e) {
    console.error('JavaScript error:', e.error);
    // Implement error reporting here
});

// Performance monitoring
if ('performance' in window) {
    window.addEventListener('load', function() {
        setTimeout(() => {
            const perfData = performance.getEntriesByType('navigation')[0];
            console.log('Page load time:', perfData.loadEventEnd - perfData.loadEventStart, 'ms');
        }, 0);
    });
}

// Export functions for global access
window.BrowserAgentDocs = {
    toggleTheme,
    performSearch,
    trackEvent
};