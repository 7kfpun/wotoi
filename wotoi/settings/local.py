""" Local develop related settings"""


from .project import *


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': op.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}

# Debug
DEBUG = True
TEMPLATE_DEBUG = DEBUG
INSTALLED_APPS += 'debug_toolbar', 'django_extensions'
MIDDLEWARE_CLASSES += 'debug_toolbar.middleware.DebugToolbarMiddleware',
INTERNAL_IPS = ['127.0.0.1', '33.33.33.10']
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

# pymode:lint_ignore=W0401
