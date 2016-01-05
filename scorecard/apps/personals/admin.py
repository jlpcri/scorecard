from django.contrib import admin

from models import InnovationStats, TestLabStats, RequirementStats, TestStats


for m in [InnovationStats, RequirementStats, TestStats, TestLabStats]:
    admin.site.register(m)
