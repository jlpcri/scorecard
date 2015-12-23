from base import *

SETTINGS_MODULE = 'scorecard.settings.qaci01'

ALLOWED_HOSTS = [
    'apps.qaci01.wic.west.com',
    'apps.qaci01'
]

HOST_URL = 'http://apps.qaci01.wic.west.com' + LOGIN_URL

DATABASES = {
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