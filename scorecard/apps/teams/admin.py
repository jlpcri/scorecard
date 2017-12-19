from django.contrib import admin

from models import (InnovationMetrics, LabMetrics, RequirementMetrics,
                    TestMetrics, TestMetricsConfiguration)

for m in [InnovationMetrics, LabMetrics, RequirementMetrics, TestMetrics, TestMetricsConfiguration]:
    admin.site.register(m)
