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

# if socket.gethostname() == 'sliu-OptiPlex-GX520':
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': 'scorecard_subteamed',
#             'USER': 'scorecard',
#             'PASSWORD': 'scorecard_development',
#             'HOST': 'qaci01.wic.west.com',
#             # 'PORT': '5432',
#             'PORT': '5433'  # another postgres instance
#         }
#     }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'scorecard',
        'USER': 'visilog',
        'PASSWORD': '6ewuON0>;wHTe(DttOwjg#5NY)U497xKVwOxmQt60A1%}r:@qC&`7OdSP8u[.l[',
        'HOST': 'linux6437.wic.west.com',
        'PORT': '5432'
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'scorecard',
#         'USER': 'ceeq',
#         'PASSWORD': 'ceeq_development',
#         'HOST': 'mydbinstance.ce8tamiymyr9.us-west-2.rds.amazonaws.com',
#         'PORT': '5432'
#     }
# }
