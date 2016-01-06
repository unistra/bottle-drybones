"""
wsgi configuration
"""

import os
os.chdir(os.path.dirname(__file__))

from environ import set_settings_module
set_settings_module()

# import application for wsgi
from server import application
