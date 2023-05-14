from os import environ, path
from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, '.env'))

class Config(object):
    # sqlalchemy
    SECRET_KEY = environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
                              # or 'sqlite:///' + path.join(BASE_DIR, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
