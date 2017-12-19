from scorecard.settings.base import *

DEBUG = True

INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INTERNAL_IPS = ['10.6.20.124','127.0.0.1']



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

DB_6437_TEST = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'scorecard_test',
        'USER': 'visilog',
        'PASSWORD': '6ewuON0>;wHTe(DttOwjg#5NY)U497xKVwOxmQt60A1%}r:@qC&`7OdSP8u[.l[',
        'HOST': 'linux6437.wic.west.com',
        'PORT': '5432'
    }
}

DATABASES = DB_6437_TEST
