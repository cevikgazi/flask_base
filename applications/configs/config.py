import logging
import os


class BaseConfig:

    SITE_TITLE = os.getenv('SITE_TITLE', 'website test')

    # JSON configuration
    JSON_AS_ASCII = False

    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')
    # Default log level
    LOG_LEVEL = logging.WARN


class TestingConfig(BaseConfig):
    """ Test configuration """
    pass


class DevelopmentConfig(BaseConfig):
    """ Development configuration """
    pass


class ProductionConfig(BaseConfig):
    """Build environment configuration"""
    LOG_LEVEL = logging.ERROR


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
