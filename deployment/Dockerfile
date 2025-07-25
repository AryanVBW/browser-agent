# Multi-stage Dockerfile for Browser Agent
# Optimized for production deployment with minimal image size

# Build stage
FROM python:3.11-slim as builder

# Set build arguments
ARG BUILD_DATE
ARG VERSION
ARG VCS_REF

# Add metadata
LABEL org.opencontainers.image.title="Browser Agent" \
      org.opencontainers.image.description="AI-powered browser automation tool" \
      org.opencontainers.image.version="${VERSION}" \
      org.opencontainers.image.created="${BUILD_DATE}" \
      org.opencontainers.image.revision="${VCS_REF}" \
      org.opencontainers.image.vendor="Browser Agent Team" \
      org.opencontainers.image.licenses="MIT" \
      org.opencontainers.image.source="https://github.com/yourusername/browser-agent" \
      org.opencontainers.image.documentation="https://browser-agent.readthedocs.io"

# Set environment variables for build
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    DEBIAN_FRONTEND=noninteractive

# Install system dependencies for building
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    g++ \
    libc6-dev \
    libffi-dev \
    libssl-dev \
    pkg-config \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip and install build tools
RUN pip install --upgrade pip setuptools wheel

# Copy requirements first for better caching
COPY requirements.txt requirements-minimal.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . /app
WORKDIR /app

# Install the application
RUN pip install --no-cache-dir -e .

# Production stage
FROM python:3.11-slim as production

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/opt/venv/bin:$PATH" \
    DEBIAN_FRONTEND=noninteractive \
    DISPLAY=:99 \
    BROWSER_AGENT_ENV=production \
    BROWSER_AGENT_LOG_LEVEL=INFO

# Install runtime system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Basic utilities
    curl \
    wget \
    unzip \
    gnupg \
    ca-certificates \
    # X11 and display
    xvfb \
    x11vnc \
    fluxbox \
    # Browser dependencies
    libnss3 \
    libatk-bridge2.0-0 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libxss1 \
    libasound2 \
    libatspi2.0-0 \
    libgtk-3-0 \
    # Fonts
    fonts-liberation \
    fonts-noto-color-emoji \
    fonts-noto-cjk \
    # Process management
    supervisor \
    # Cleanup
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Install Chrome
RUN curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Install Firefox
RUN curl -fsSL https://packages.mozilla.org/apt/repo-signing-key.gpg | gpg --dearmor -o /usr/share/keyrings/packages.mozilla.org.gpg \
    && echo "deb [signed-by=/usr/share/keyrings/packages.mozilla.org.gpg] https://packages.mozilla.org/apt mozilla main" > /etc/apt/sources.list.d/mozilla.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends firefox \
    && rm -rf /var/lib/apt/lists/*

# Create application user
RUN groupadd -r browseragent && useradd -r -g browseragent -s /bin/bash browseragent

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Copy application code
COPY --from=builder /app /app
WORKDIR /app

# Create necessary directories
RUN mkdir -p /app/logs /app/screenshots /app/exports /app/temp /app/cache \
    /app/browser_profiles /app/user_data /home/browseragent/.config \
    && chown -R browseragent:browseragent /app /home/browseragent

# Install Playwright browsers
RUN python -m playwright install chromium firefox webkit \
    && python -m playwright install-deps

# Copy configuration files
COPY docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY docker/xvfb.conf /etc/supervisor/conf.d/xvfb.conf
COPY docker/entrypoint.sh /entrypoint.sh
COPY docker/healthcheck.sh /healthcheck.sh

# Make scripts executable
RUN chmod +x /entrypoint.sh /healthcheck.sh

# Switch to application user
USER browseragent

# Set working directory
WORKDIR /app

# Expose ports
EXPOSE 8080 5900 6080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD /healthcheck.sh

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Default command
CMD ["gui"]

# Development stage
FROM production as development

# Switch back to root for development setup
USER root

# Install development dependencies
COPY requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements-dev.txt

# Install additional development tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    vim \
    nano \
    htop \
    tree \
    git \
    ssh \
    && rm -rf /var/lib/apt/lists/*

# Install pre-commit hooks
RUN pre-commit install || true

# Set development environment variables
ENV BROWSER_AGENT_ENV=development \
    BROWSER_AGENT_LOG_LEVEL=DEBUG \
    BROWSER_AGENT_DEBUG=1

# Switch back to application user
USER browseragent

# Development command
CMD ["development"]

# Testing stage
FROM development as testing

# Switch to root for test setup
USER root

# Install test dependencies
RUN pip install --no-cache-dir pytest pytest-cov pytest-xdist pytest-mock

# Copy test files
COPY tests/ /app/tests/
RUN chown -R browseragent:browseragent /app/tests

# Switch back to application user
USER browseragent

# Test command
CMD ["pytest", "-v", "--cov=brouser_agent", "--cov-report=term-missing"]

# Minimal stage for production deployment
FROM python:3.11-alpine as minimal

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/opt/venv/bin:$PATH"

# Install minimal runtime dependencies
RUN apk add --no-cache \
    chromium \
    chromium-chromedriver \
    firefox \
    xvfb \
    supervisor \
    curl

# Create application user
RUN addgroup -g 1000 browseragent && \
    adduser -D -s /bin/sh -u 1000 -G browseragent browseragent

# Copy virtual environment and application
COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /app /app

# Set ownership
RUN chown -R browseragent:browseragent /app

# Switch to application user
USER browseragent
WORKDIR /app

# Minimal entrypoint
CMD ["python", "-m", "brouser_agent.cli_main"]

# Multi-architecture build support
# Use buildx for cross-platform builds:
# docker buildx build --platform linux/amd64,linux/arm64 -t browser-agent .

# Build arguments for customization
ARG PYTHON_VERSION=3.11
ARG CHROME_VERSION=stable
ARG FIREFOX_VERSION=latest
ARG PLAYWRIGHT_VERSION=latest

# Environment variables that can be overridden at runtime
ENV BROWSER_AGENT_CONFIG_DIR=/app/config \
    BROWSER_AGENT_DATA_DIR=/app/data \
    BROWSER_AGENT_LOG_DIR=/app/logs \
    BROWSER_AGENT_CACHE_DIR=/app/cache \
    BROWSER_AGENT_TEMP_DIR=/app/temp \
    BROWSER_AGENT_SCREENSHOTS_DIR=/app/screenshots \
    BROWSER_AGENT_EXPORTS_DIR=/app/exports \
    BROWSER_AGENT_BROWSER_PROFILES_DIR=/app/browser_profiles \
    BROWSER_AGENT_PLUGINS_DIR=/app/plugins \
    BROWSER_AGENT_DEFAULT_BROWSER=chrome \
    BROWSER_AGENT_HEADLESS=true \
    BROWSER_AGENT_TIMEOUT=30 \
    BROWSER_AGENT_MAX_WORKERS=4 \
    BROWSER_AGENT_ENABLE_LOGGING=true \
    BROWSER_AGENT_ENABLE_SCREENSHOTS=true \
    BROWSER_AGENT_ENABLE_EXPORTS=true

# Volume mounts for persistent data
VOLUME ["/app/data", "/app/logs", "/app/screenshots", "/app/exports", "/app/browser_profiles"]

# Security settings
RUN echo "browseragent:x:1000:1000:Browser Agent User:/home/browseragent:/bin/bash" >> /etc/passwd && \
    echo "browseragent:x:1000:" >> /etc/group

# Final stage selection based on build target
# Default to production if no target specified
FROM production