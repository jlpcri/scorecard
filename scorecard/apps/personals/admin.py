from django.contrib import admin

from models import InnovationStats, LabStats, RequirementStats, TestStats


for m in [InnovationStats, RequirementStats, TestStats, LabStats]:
    admin.site.register(m)
