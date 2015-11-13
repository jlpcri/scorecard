from django.contrib import admin

from models import InnovationMetrics, LabMetrics, RequirementMetrics, TestMetrics


for m in [InnovationMetrics, LabMetrics, RequirementMetrics, TestMetrics]:
    admin.site.register(m)
