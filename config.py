import os
from environs import Env

env = Env()
env.read_env()

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = env.str('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Limit file caching
SEND_FILE_MAX_AGE_DEFAULT = 0

# CSRF token lasts till end of current session
WTF_CSRF_TIME_LIMIT = None
