class Config(object):
    pass

class ProdConfig(object):
    pass

class DevConfig(object):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:ajaxAJAX1000?@localhost:3306/testdulceria"

