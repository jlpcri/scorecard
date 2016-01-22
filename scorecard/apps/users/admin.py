from django.contrib import admin

from models import FunctionalGroup, HumanResource, ColumnPreference


for m in [FunctionalGroup, HumanResource]:
    admin.site.register(m)

admin.site.register(ColumnPreference)
admin.site.register(ColumnPreference)
