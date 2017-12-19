import socket

from base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# STATIC_URL = 'http://apps.qaci01.wic.west.com/static/'
# STATIC_URL = 'http://10.6.20.109/static/'

# used for sending email
HOST_URL = 'http://10.6.20.106:8000' + LOGIN_URL
# HOST_URL = 'http://apps.qaci01.wic.west.com' + LOGIN_URL


if socket.gethostname() == 'sliu-OptiPlex-GX520':
    INSTALLED_APPS += ('debug_toolbar', )
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )
    INTERNAL_IPS = ['127.0.0.1', '10.6.20.127', '10.27.170.225']

DB_QACI01 = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'scorecard',
        'USER': 'scorecard',
        'PASSWORD': 'scorecard_development',
        'HOST': 'qaci01.wic.west.com',
        # 'PORT': '5432',
        'PORT': '5433'  # another postgres instance
    }
}

DB_6437 = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'scorecard',
        'USER': 'visilog',
        'PASSWORD': '6ewuON0>;wHTe(DttOwjg#5NY)U497xKVwOxmQt60A1%}r:@qC&`7OdSP8u[.l[',
        'HOST': 'linux6437.wic.west.com',
        'PORT': '5432'
    }
}

DB_DOCKER = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': '5432'
    }
}

DATABASES = DB_6437
