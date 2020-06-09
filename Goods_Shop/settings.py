

class Config(object):
    # session_key
    SECRET_KEY = 'asdfg'
    # md5_key
    SALT = b'jdbhjb'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:1234@127.0.0.1:3306/shop?charset=utf8"
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_MAX_OVERFLOW = 5

    SQLALCHEMY_TRACK_MODIFICATIONS = False