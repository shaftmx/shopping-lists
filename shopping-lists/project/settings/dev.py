from .base import *

DEBUG = TEMPLATE_DEBUG = False

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': 'dev.db',
#    }
#}
DATABASES = { 
    'default': {
        'NAME': 'courses',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'courses',
        'PASSWORD': 'Noob123',
        'HOST': 'localhost',
    }   
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Disable caching while in development
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Add SQL statement logging in development
LOGGING['loggers']['django.db'] = {
    'handlers': ['console'],
    'level': 'DEBUG',
    'propagate': False
}

# set up Django Debug Toolbar if installed
#try:
#    import debug_toolbar  # noqa
#    MIDDLEWARE_CLASSES += (
#        'debug_toolbar.middleware.DebugToolbarMiddleware',
#    )
#    INSTALLED_APPS += (
#        'debug_toolbar',
#    )
#    DEBUG_TOOLBAR_CONFIG = {
#        'INTERCEPT_REDIRECTS': False,
#        'SHOW_TOOLBAR_CALLBACK': lambda *args, **kwargs: True
#    }
#except ImportError:
#    pass


# Set up django-extensions if installed
try:
    import django_extensions  # noqa
    INSTALLED_APPS += ('django_extensions',
    'shop',
    )
except ImportError:
    pass
