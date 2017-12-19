from base import *

SETTINGS_MODULE = 'scorecard.settings.qaci01'

ALLOWED_HOSTS = [
    'apps.qaci01.wic.west.com',
    'apps.qaci01'
]

HOST_URL = 'http://apps.qaci01.wic.west.com' + LOGIN_URL
EMAIL_HOST = 'linux745.wic.west.com'
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'QEIInnovation@west.com'

DEBUG = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'scorecard_subteamed',
#         'USER': 'scorecard',
#         'PASSWORD': 'scorecard_development',
#         'HOST': 'qaci01.wic.west.com',
#         # 'PORT': '5432',
#         'PORT': '5433'  # another postgres instance
#     }
# }

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
