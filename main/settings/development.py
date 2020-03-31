"""
    Specific settings for development environment
"""

import os

# Specific case that use import *
from .base import *

DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost',
]
CORS_ORIGIN_REGEX_WHITELIST = [
    'http://localhost',
]