// Advanced Search Functionality for Browser Agent Documentation

// Search configuration
const SEARCH_CONFIG = {
    minQueryLength: 2,
    maxResults: 10,
    debounceDelay: 300,
    highlightClass: 'search-highlight',
    resultClass: 'search-result-item'
};

// Search index structure
let searchIndex = {
    pages: [],
    sections: [],
    keywords: new Map(),
    isLoaded: false
};

// Initialize search system
function initializeAdvancedSearch() {
    buildSearchIndex();
    setupSearchUI();
    setupKeyboardShortcuts();
}

// Build comprehensive search index
function buildSearchIndex() {
    const pages = [
        {
            id: 'home',
            title: 'Browser Agent - AI-Powered Web Automation',
            url: './index.html',
            description: 'Revolutionary AI-driven browser automation with multi-LLM support, MCP integration, and natural language processing.',
            keywords: ['browser', 'automation', 'ai', 'web', 'selenium', 'playwright', 'vivek wagdare', 'aryanvbw'],
            category: 'overview',
            priority: 10
        },
        {
            id: 'quick-start',
            title: 'Quick Start Guide',
            url: './pages/quick-start.html',
            description: 'Get up and running with Browser Agent in minutes. Step-by-step installation and first automation.',
            keywords: ['quick', 'start', 'getting started', 'installation', 'setup', 'tutorial', 'beginner'],
            category: 'getting-started',
            priority: 9
        },
        {
            id: 'installation',
            title: 'Installation & Setup',
            url: './pages/installation.html',
            description: 'Complete installation guide for Windows, macOS, Linux, Docker, and cloud environments.',
            keywords: ['install', 'setup', 'docker', 'pip', 'requirements', 'dependencies', 'environment'],
            category: 'setup',
            priority: 8
        },
        {
            id: 'features',
            title: 'Features & Use Cases',
            url: './pages/features.html',
            description: 'Explore all features including multi-browser support, AI integration, and real-world automation scenarios.',
            keywords: ['features', 'capabilities', 'multi-browser', 'chrome', 'firefox', 'safari', 'edge', 'use cases'],
            category: 'features',
            priority: 7
        },
        {
            id: 'mcp-integration',
            title: 'MCP Integration',
            url: './pages/mcp-integration.html',
            description: 'Model Context Protocol integration, external tool connections, and workflow automation.',
            keywords: ['mcp', 'model context protocol', 'integration', 'tools', 'plugins', 'n8n', 'figma'],
            category: 'integration',
            priority: 6
        },
        {
            id: 'ai-integration',
            title: 'AI & LLM Integration',
            url: './pages/ai-integration.html',
            description: 'OpenAI GPT, Claude, and Gemini integration for natural language automation.',
            keywords: ['ai', 'llm', 'openai', 'claude', 'gemini', 'gpt', 'natural language', 'chatgpt'],
            category: 'ai',
            priority: 6
        },
        {
            id: 'api',
            title: 'API Reference',
            url: './pages/api.html',
            description: 'Complete API documentation, plugin development guide, and code examples.',
            keywords: ['api', 'reference', 'documentation', 'plugins', 'development', 'sdk', 'python'],
            category: 'reference',
            priority: 5
        },
        {
            id: 'troubleshooting',
            title: 'Troubleshooting & Debugging',
            url: './pages/troubleshooting.html',
            description: 'Common issues, debugging tips, error solutions, and performance optimization.',
            keywords: ['troubleshooting', 'debug', 'issues', 'problems', 'solutions', 'errors', 'performance'],
            category: 'support',
            priority: 4
        },
        {
            id: 'examples',
            title: 'Examples & Tutorials',
            url: './pages/examples.html',
            description: 'Real-world examples, code samples, and step-by-step tutorials.',
            keywords: ['examples', 'tutorials', 'code', 'samples', 'demos', 'use cases', 'automation scripts'],
            category: 'examples',
            priority: 4
        },
        {
            id: 'faq',
            title: 'FAQ & Community',
            url: './pages/faq.html',
            description: 'Frequently asked questions, community resources, and support channels.',
            keywords: ['faq', 'questions', 'community', 'support', 'help', 'forum', 'discord'],
            category: 'support',
            priority: 3
        },
        {
            id: 'contributing',
            title: 'Contributing Guide',
            url: './pages/contributing.html',
            description: 'How to contribute to Browser Agent, development setup, and coding guidelines.',
            keywords: ['contributing', 'development', 'github', 'pull request', 'open source', 'collaboration'],
            category: 'development',
            priority: 2
        },
        {
            id: 'changelog',
            title: 'Changelog & Releases',
            url: './pages/changelog.html',
            description: 'Version history, release notes, and feature updates.',
            keywords: ['changelog', 'releases', 'version', 'updates', 'history', 'new features'],
            category: 'reference',
            priority: 2
        }
    ];

    const sections = [
        {
            id: 'multi-browser',
            title: 'Multi-Browser Support',
            pageId: 'features',
            description: 'Chrome, Firefox, Safari, and Edge support with unified API',
            keywords: ['multi-browser', 'chrome', 'firefox', 'safari', 'edge', 'unified api']
        },
        {
            id: 'ai-powered',
            title: 'AI-Powered Automation',
            pageId: 'features',
            description: 'Natural language processing with multiple AI models',
            keywords: ['ai powered', 'natural language', 'intelligent automation', 'smart']
        },
        {
            id: 'docker-setup',
            title: 'Docker Installation',
            pageId: 'installation',
            description: 'Container-based deployment and cloud-ready setup',
            keywords: ['docker', 'container', 'deployment', 'cloud', 'kubernetes']
        },
        {
            id: 'python-api',
            title: 'Python API',
            pageId: 'api',
            description: 'Complete Python SDK and API reference',
            keywords: ['python', 'sdk', 'api', 'programming', 'code']
        }
    ];

    // Build keyword index
    const keywordIndex = new Map();
    
    pages.forEach(page => {
        page.keywords.forEach(keyword => {
            if (!keywordIndex.has(keyword)) {
                keywordIndex.set(keyword, []);
            }
            keywordIndex.get(keyword).push({
                type: 'page',
                id: page.id,
                priority: page.priority
            });
        });
    });
    
    sections.forEach(section => {
        section.keywords.forEach(keyword => {
            if (!keywordIndex.has(keyword)) {
                keywordIndex.set(keyword, []);
            }
            keywordIndex.get(keyword).push({
                type: 'section',
                id: section.id,
                priority: 5
            });
        });
    });

    searchIndex = {
        pages,
        sections,
        keywords: keywordIndex,
        isLoaded: true
    };

    console.log('Search index built with', pages.length, 'pages and', sections.length, 'sections');
}

// Setup search UI components
function setupSearchUI() {
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');
    
    if (!searchInput || !searchResults) return;

    let searchTimeout;
    let currentQuery = '';
    let selectedIndex = -1;

    // Input event handler with debouncing
    searchInput.addEventListener('input', function(e) {
        clearTimeout(searchTimeout);
        const query = e.target.value.trim();
        currentQuery = query;
        selectedIndex = -1;

        if (query.length < SEARCH_CONFIG.minQueryLength) {
            hideSearchResults();
            return;
        }

        searchTimeout = setTimeout(() => {
            if (currentQuery === query) { // Ensure query hasn't changed
                performAdvancedSearch(query);
            }
        }, SEARCH_CONFIG.debounceDelay);
    });

    // Focus event handler
    searchInput.addEventListener('focus', function() {
        if (this.value.trim().length >= SEARCH_CONFIG.minQueryLength) {
            showSearchResults();
        }
    });

    // Keyboard navigation
    searchInput.addEventListener('keydown', function(e) {
        const results = searchResults.querySelectorAll('.search-result-item');
        
        switch(e.key) {
            case 'ArrowDown':
                e.preventDefault();
                selectedIndex = Math.min(selectedIndex + 1, results.length - 1);
                updateSelection(results);
                break;
                
            case 'ArrowUp':
                e.preventDefault();
                selectedIndex = Math.max(selectedIndex - 1, -1);
                updateSelection(results);
                break;
                
            case 'Enter':
                e.preventDefault();
                if (selectedIndex >= 0 && results[selectedIndex]) {
                    const link = results[selectedIndex].querySelector('a');
                    if (link) {
                        window.location.href = link.href;
                    }
                }
                break;
                
            case 'Escape':
                hideSearchResults();
                searchInput.blur();
                break;
        }
    });

    // Click outside to close
    document.addEventListener('click', function(e) {
        if (!searchInput.contains(e.target) && !searchResults.contains(e.target)) {
            hideSearchResults();
        }
    });

    function updateSelection(results) {
        results.forEach((result, index) => {
            result.classList.toggle('selected', index === selectedIndex);
        });
    }
}

// Advanced search algorithm
function performAdvancedSearch(query) {
    if (!searchIndex.isLoaded) {
        console.warn('Search index not loaded');
        return;
    }

    const results = [];
    const queryLower = query.toLowerCase();
    const queryWords = queryLower.split(/\s+/).filter(word => word.length > 0);

    // Search pages
    searchIndex.pages.forEach(page => {
        const score = calculateRelevanceScore(page, queryWords, queryLower);
        if (score > 0) {
            results.push({
                ...page,
                type: 'page',
                score,
                matchedTerms: findMatchedTerms(page, queryWords)
            });
        }
    });

    // Search sections
    searchIndex.sections.forEach(section => {
        const score = calculateRelevanceScore(section, queryWords, queryLower);
        if (score > 0) {
            const parentPage = searchIndex.pages.find(p => p.id === section.pageId);
            results.push({
                ...section,
                type: 'section',
                score,
                parentPage,
                matchedTerms: findMatchedTerms(section, queryWords)
            });
        }
    });

    // Sort by relevance score
    results.sort((a, b) => b.score - a.score);

    // Limit results
    const limitedResults = results.slice(0, SEARCH_CONFIG.maxResults);

    displayAdvancedSearchResults(limitedResults, query);
}

// Calculate relevance score for search results
function calculateRelevanceScore(item, queryWords, fullQuery) {
    let score = 0;
    const titleLower = item.title.toLowerCase();
    const descLower = item.description.toLowerCase();
    const keywordsLower = item.keywords.map(k => k.toLowerCase());

    // Exact title match (highest priority)
    if (titleLower.includes(fullQuery)) {
        score += 100;
    }

    // Title word matches
    queryWords.forEach(word => {
        if (titleLower.includes(word)) {
            score += 50;
        }
    });

    // Description matches
    queryWords.forEach(word => {
        if (descLower.includes(word)) {
            score += 20;
        }
    });

    // Keyword matches
    queryWords.forEach(word => {
        keywordsLower.forEach(keyword => {
            if (keyword.includes(word)) {
                score += 30;
            }
        });
    });

    // Priority boost
    if (item.priority) {
        score += item.priority;
    }

    // Partial matches
    queryWords.forEach(word => {
        if (word.length >= 3) {
            if (titleLower.includes(word.substring(0, 3))) {
                score += 10;
            }
        }
    });

    return score;
}

// Find matched terms for highlighting
function findMatchedTerms(item, queryWords) {
    const matched = [];
    const searchText = `${item.title} ${item.description} ${item.keywords.join(' ')}`.toLowerCase();
    
    queryWords.forEach(word => {
        if (searchText.includes(word)) {
            matched.push(word);
        }
    });
    
    return matched;
}

// Display search results with enhanced formatting
function displayAdvancedSearchResults(results, query) {
    const searchResults = document.getElementById('search-results');
    
    if (results.length === 0) {
        searchResults.innerHTML = `
            <div class="search-no-results">
                <div class="no-results-icon">🔍</div>
                <h4>No results found</h4>
                <p>Try different keywords or check our <a href="./pages/faq.html">FAQ</a> for help</p>
            </div>
        `;
    } else {
        const resultsHTML = results.map((result, index) => {
            const icon = getResultIcon(result.type, result.category);
            const highlightedTitle = highlightMatches(result.title, result.matchedTerms);
            const highlightedDesc = highlightMatches(result.description, result.matchedTerms);
            const categoryBadge = result.category ? `<span class="result-category">${result.category}</span>` : '';
            const parentInfo = result.parentPage ? `<span class="result-parent">in ${result.parentPage.title}</span>` : '';
            
            return `
                <div class="search-result-item" data-index="${index}">
                    <a href="${result.url}" class="result-link">
                        <div class="result-header">
                            <span class="result-icon">${icon}</span>
                            <div class="result-meta">
                                ${categoryBadge}
                                ${parentInfo}
                            </div>
                        </div>
                        <h4 class="result-title">${highlightedTitle}</h4>
                        <p class="result-description">${highlightedDesc}</p>
                        <div class="result-footer">
                            <span class="result-type">${result.type}</span>
                            <span class="result-score">Score: ${result.score}</span>
                        </div>
                    </a>
                </div>
            `;
        }).join('');
        
        searchResults.innerHTML = `
            <div class="search-results-header">
                <span class="results-count">${results.length} result${results.length !== 1 ? 's' : ''} for "${query}"</span>
            </div>
            ${resultsHTML}
        `;
    }
    
    showSearchResults();
}

// Get appropriate icon for result type
function getResultIcon(type, category) {
    const icons = {
        page: '📄',
        section: '📝',
        overview: '🏠',
        'getting-started': '🚀',
        setup: '⚙️',
        features: '⭐',
        integration: '🔌',
        ai: '🤖',
        reference: '📚',
        support: '❓',
        examples: '💡',
        development: '👨‍💻'
    };
    
    return icons[category] || icons[type] || '📄';
}

// Highlight matched terms in text
function highlightMatches(text, matchedTerms) {
    if (!matchedTerms || matchedTerms.length === 0) {
        return text;
    }
    
    let highlightedText = text;
    matchedTerms.forEach(term => {
        const regex = new RegExp(`(${escapeRegExp(term)})`, 'gi');
        highlightedText = highlightedText.replace(regex, `<mark class="${SEARCH_CONFIG.highlightClass}">$1</mark>`);
    });
    
    return highlightedText;
}

// Escape special regex characters
function escapeRegExp(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

// Setup keyboard shortcuts
function setupKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + K to focus search
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            const searchInput = document.getElementById('search-input');
            if (searchInput) {
                searchInput.focus();
                searchInput.select();
            }
        }
        
        // Escape to close search
        if (e.key === 'Escape') {
            hideSearchResults();
        }
    });
}

// Show/hide search results
function showSearchResults() {
    const searchResults = document.getElementById('search-results');
    if (searchResults) {
        searchResults.style.display = 'block';
        searchResults.classList.add('visible');
    }
}

function hideSearchResults() {
    const searchResults = document.getElementById('search-results');
    if (searchResults) {
        searchResults.style.display = 'none';
        searchResults.classList.remove('visible');
    }
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeAdvancedSearch);
} else {
    initializeAdvancedSearch();
}

// Export for global access
window.AdvancedSearch = {
    performAdvancedSearch,
    buildSearchIndex,
    searchIndex
};