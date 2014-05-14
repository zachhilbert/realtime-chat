class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '+\x97\x1e\x11 [\xfd\xb2\xe3\xe0\xa5,\xbb\xe1\x8c\xf5:\x87\xdd\xfb\x95\xd5\x83}'
    SQLALCHEMY_DATABASE_URI = 'postgresql://<username>:<password>/r_chat'
    SOCKET_IO_PORT = 5000

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
