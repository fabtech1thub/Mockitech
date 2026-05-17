"""
Production configuration for MockiTech Flask application
Use this in cPanel environment
"""

import os

class ProductionConfig:
    """Production environment configuration"""
    
    # Core settings
    DEBUG = False
    TESTING = False
    ENV = 'production'
    
    # Security
    PROPAGATE_EXCEPTIONS = True
    PRESERVE_CONTEXT_ON_EXCEPTION = True
    
    # Session security
    SESSION_COOKIE_SECURE = True  # Only send over HTTPS
    SESSION_COOKIE_HTTPONLY = True  # Prevent JavaScript access
    SESSION_COOKIE_SAMESITE = 'Lax'  # CSRF protection
    
    # Allowed hosts (update with your domain)
    PREFERRED_URL_SCHEME = 'https'
    
    # Cache settings
    SEND_FILE_MAX_AGE_DEFAULT = 31536000  # 1 year for static files
    
    # Template settings
    TEMPLATES_AUTO_RELOAD = False
    
    # JSON settings
    JSON_SORT_KEYS = False

class DevelopmentConfig:
    """Development environment configuration"""
    
    DEBUG = True
    TESTING = False
    ENV = 'development'
    
    # Allow all hosts in development
    PREFERRED_URL_SCHEME = 'http'
    
    # Reload templates for quick changes
    TEMPLATES_AUTO_RELOAD = True
    
    # Disable some security checks in development
    SESSION_COOKIE_SECURE = False

# Get config based on environment
def get_config():
    """Return appropriate config based on FLASK_ENV"""
    env = os.getenv('FLASK_ENV', 'development')
    if env == 'production':
        return ProductionConfig
    return DevelopmentConfig
