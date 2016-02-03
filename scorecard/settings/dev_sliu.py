import socket
from base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# STATIC_URL = 'http://apps.qaci01.wic.west.com/static/'
# STATIC_URL = 'http://10.6.20.109/static/'

# used for sending email
# HOST_URL = 'http://10.6.20.109:8000' + LOGIN_URL
HOST_URL = 'http://apps.qaci01.wic.west.com' + LOGIN_URL

if socket.gethostname() == 'sliu-OptiPlex-GX520':
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