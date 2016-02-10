from django.contrib import admin

from models import Automation

for m in [Automation]:
    admin.site.register(m)
