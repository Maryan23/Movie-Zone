class Config:
    UPLOADED_PHOTOS_DEST = 'app/static/Photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProdConfig(Config):
    DEBUG=True

class DevConfig(Config):
    DEBUG=True

config_options = {
    "production" : ProdConfig,
    "development": DevConfig
}