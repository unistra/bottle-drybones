from bottle import route, default_app
from environ import settings
from log import logger


@route('/')
def home():
    logger.info("Start {{cookiecutter.project_name}}")
    return "{{cookiecutter.project_name}} home: " + settings('MY_CUSTOM_PARAM')

application = default_app()
