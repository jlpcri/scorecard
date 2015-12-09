from base import *

SETTINGS_MODULE = 'scorecard.settings.qaci01'

ALLOWED_HOSTS = [
    'apps.qaci01.wic.west.com',
    'apps.qaci01'
]

HOST_URL = 'http://apps.qaci01.wic.west.com' + LOGIN_URL

#----------------GMAIL Backend----------------
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ceeqwic@gmail.com'
EMAIL_HOST_PASSWORD = '^S=+c3gyYu6F74D'
EMAIL_PORT = 587
