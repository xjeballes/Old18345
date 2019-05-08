import os

postgres_local_base = "postgresql://postgres:18345@localhost:5432/BoopIt"

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "bof")
    DEBUG = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:18345@localhost:5432/BoopIt"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:18345@localhost:5432/BoopTest"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgres://mvuhirpwnegrfx:a69aaad86a582680767f5c945c437e5ce3bea8229da158df47633f395c04a2b3@ec2-54-235-167-210.compute-1.amazonaws.com:5432/d55v4lf0t9v2sp"

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
key = Config.SECRET_KEY

