from .base import *  # noqa

INSTALLED_APPS +=[  # noqa
    'django_extensions',
    'debug_toolbar',
]

MIDDLEWARE += [  # noqa
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

LANGUAGE_CODE = 'es'

DEBUG = True
