# /src/config.py
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    GRAPHQL_API = os.getenv('GRAPHQL_API')



class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    GRAPHQL_API = os.getenv('GRAPHQL_API')

app_config = {
    'development': Development,
    'production': Production,
}
