import os

postgres_local_base = "postgresql://postgres:18345@localhost:5432/BoopIt"

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "bof")
    DEBUG = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:18345@localhost:5432/BoopIt"
    CLOUDINARY_URL = "cloudinary://231339544622852:cR3RImpJd8njjhS8-zO5GDRacO4@fmscrns"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:18345@localhost:5432/BoopTest"
    CLOUDINARY_URL = "cloudinary://231339544622852:cR3RImpJd8njjhS8-zO5GDRacO4@fmscrns"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:18345@localhost:5432/BoopIt"
    CLOUDINARY_URL = "cloudinary://231339544622852:cR3RImpJd8njjhS8-zO5GDRacO4@fmscrns"

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
key = Config.SECRET_KEY

