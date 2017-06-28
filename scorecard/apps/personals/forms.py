from django import forms
from django.forms import ModelForm

from models import InnovationStats, LabStats, RequirementStats, TestStats


class InnovationForm(ModelForm):
    class Meta:
        model = InnovationStats
        exclude = ['created', 'confirmed', 'updated', 'human_resource']


class LabForm(ModelForm):
    class Meta:
        model = LabStats
        exclude = ['created', 'confirmed', 'updated', 'human_resource']


class RequirementForm(ModelForm):
    class Meta:
        model = RequirementStats
        exclude = ['created', 'confirmed', 'updated', 'human_resource', 'elicitation_analysis_time', 'research_time', 'resource_swap_time']


class TestForm(ModelForm):
    class Meta:
        model = TestStats
        exclude = ['created', 'confirmed', 'updated', 'human_resource']
