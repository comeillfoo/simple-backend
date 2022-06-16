"""it is a config module."""
import os


class Config(object):
    """Main config for the whole flask app."""

    DEBUG = os.environ.get('DEBUG')
    ENV = os.environ.get('FLASK_ENV')
    APP = os.environ.get('FLASK_APP')
