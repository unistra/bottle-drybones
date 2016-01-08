"""
Define the logger
"""

import logging
from environ import settings

# create logger
logger = logging.getLogger('{{cookiecutter.repo_name}}')
logger.setLevel(logging.INFO)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# file handler
fh = logging.FileHandler(settings('LOG_FILE'))
fh.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - \
%(message)s')

# add formatter
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)
