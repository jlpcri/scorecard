from django.contrib import admin

from models import FunctionalGroup, HumanResource


for m in [FunctionalGroup, HumanResource]:
    admin.site.register(m)
