from django.contrib import admin

from models import ColumnPreference, FunctionalGroup, HumanResource, Subteam

for m in [FunctionalGroup, HumanResource, Subteam]:
    admin.site.register(m)

admin.site.register(ColumnPreference)
