"""
Preprod conf
"""
from .base import *
from os.path import dirname, join, abspath

LOG_FILE = join(dirname(dirname(dirname(abspath(__file__)))), "log", '{{cookiecutter.repo_name}}.log')

MY_CUSTOM_PARAM = "Hello World!"
