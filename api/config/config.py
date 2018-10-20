"""
Module for configuring server environment variables
"""

class Config:
    """
    Default environment configuration
    """
    TESTING = False

class Development(Config):
    """
    Development environment configuration
    """
    DEBUG = True
    ENV = 'development'

class Production(Config):
    """
    Production environment configuration
    """
    DEBUG = False
    ENV = 'production'

APP_CONFIG = {
    'development': Development,
    'production': Production,
}
