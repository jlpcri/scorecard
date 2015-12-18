from base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# STATIC_URL = 'http://apps.qaci01.wic.west.com/static/'
STATIC_URL = 'http://10.6.20.109/static/'

# used for sending email
# HOST_URL = 'http://10.6.20.109:8000' + LOGIN_URL
HOST_URL = 'http://apps.qaci01.wic.west.com' + LOGIN_URL

# #----------------GMAIL Backend----------------
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'ceeqwic@gmail.com'
# EMAIL_HOST_PASSWORD = '^S=+c3gyYu6F74D'
# EMAIL_PORT = 587
