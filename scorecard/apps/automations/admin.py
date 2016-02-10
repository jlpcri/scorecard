from django.contrib import admin

from models import InnovationAutomation, LabAutomation, RequirementAutomation, TestAutomation

for m in [InnovationAutomation, LabAutomation, RequirementAutomation, TestAutomation]:
    admin.site.register(m)
