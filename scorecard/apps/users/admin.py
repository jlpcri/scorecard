from django.contrib import admin

from models import FunctionalGroup, HumanResource, ColumnPreference, Subteam


for m in [FunctionalGroup, HumanResource, Subteam]:
    admin.site.register(m)

admin.site.register(ColumnPreference)
