import os


class Config(object):
    TEST = True

class ProductionConfig(Config):
    DATABASE_URL = os.getenv("DATABASE_URL")

class DevelopementConfig(Config):
    DATABASE_URL = "sql:///memory"
    TESTING = True