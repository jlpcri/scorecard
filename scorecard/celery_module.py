import os
import socket
from django.conf import settings

from celery import Celery

if socket.gethostname() == "sliu-OptiPlex-GX520":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scorecard.settings.local')
elif socket.gethostname() == 'qaci01':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scorecard.settings.qaci01')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scorecard.settings.base')

app = Celery('scorecard')
app.config_from_object('scorecard.celery_config')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, related_name='tasks')
