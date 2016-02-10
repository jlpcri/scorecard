from django import forms
from django.forms import ModelForm

from models import InnovationAutomation, LabAutomation, RequirementAutomation, TestAutomation


class InnovationForm(ModelForm):
    class Meta:
        model = InnovationAutomation
        exclude = ['last_success', 'last_failure', 'last_successful_run']
