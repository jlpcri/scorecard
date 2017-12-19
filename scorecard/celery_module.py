import os
import socket

from celery import Celery
from django.conf import settings

if socket.gethostname() == "sliu-OptiPlex-GX520":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scorecard.settings.local')
elif socket.gethostname() == "seenaomi-HP-Compaq-6005-Pro-SFF-PC":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scorecard.settings.dev_see')
elif socket.gethostname() == "mohan@mohan-HP-Compaq-6005-Pro-SFF-PC":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scorecard.settings.dev_mohan')
elif socket.gethostname() == 'qaci01':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scorecard.settings.qaci01')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scorecard.settings.base')

app = Celery('scorecard')
app.config_from_object('scorecard.celery_config')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, related_name='tasks')
