from django import forms
from django.forms import ModelForm
from models import TestMetrics, InnovationMetrics, LabMetrics, RequirementMetrics


class InnovationForm(ModelForm):
    class Meta:
        model = InnovationMetrics
