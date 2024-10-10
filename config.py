"""Flask App configuration."""
from os import environ, path
from dotenv import load_dotenv

# Specificy and load the `.env` file containing key/value config values
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Set Flask config variables."""
    SECRET_KEY = environ.get('SECRET_KEY')


    
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SESSION_SQLALCHEMY = environ.get('SESSION_SQLALCHEMY')