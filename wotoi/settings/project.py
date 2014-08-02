""" Project settings"""


from .core import *


INSTALLED_APPS += (
    # Community apps
    'rest_framework',
    'rest_framework.urls',
    'south',

    # Project apps
    'wotoi.api',
    'wotoi.core',
)

AUTH_USER_MODEL = 'core.CustomUser'

# pymode:lint_ignore=W0401
