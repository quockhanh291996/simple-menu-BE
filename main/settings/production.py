"""
    Specific settings for production environment
"""

# Just for demo, we don't need production on demo app :D

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    '*',
]
CORS_ORIGIN_REGEX_WHITELIST = [
    '*',
]
