class Config:
    UPLOADED_PHOTOS_DEST = 'app/static/Photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:4543@localhost/moviezone'
class ProdConfig(Config):
    DEBUG=True

class DevConfig(Config):
    DEBUG=True

config_options = {
    "production" : ProdConfig,
    "development": DevConfig
}