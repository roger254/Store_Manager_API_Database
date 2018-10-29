import os


class Configuration(object):
    """Config Class """
    DEBUG = False
    CSRF_ENABLED = True
    DB_HOST = os.getenv('DB_HOST')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfiguration(Configuration):
    """For Dev"""
    DEBUG = True


class TestingConfiguration(Configuration):
    """Test Configuration"""
    TESTING = True
    DEBUG = True
    DB_NAME = os.getenv('DB_TEST_NAME')


class ProductionConfiguration(Configuration):
    """For Production Stage"""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfiguration,
    'testing': TestingConfiguration,
    'production': ProductionConfiguration,
}
