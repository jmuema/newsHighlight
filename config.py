import os

class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_BASE_URL="https://newsapi.org/v2/sources?&language=en&apiKey=e72559e253574c5d9483430f9f9bc7d6"

    ARTICLE_API_BASE_URL="https://newsapi.org/v2/everything?sources={}&apiKey=e72559e253574c5d9483430f9f9bc7d6"

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
class ProdConfig(Config):
    '''
    Production This is a configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    ENV = 'development'

config_options = {
'development':DevConfig,
'production':ProdConfig
}