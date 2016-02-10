from django import forms
from django.forms import ModelForm

from models import Automation


class AutomationNewForm(ModelForm):
    class Meta:
        model = Automation
        fields = ['functional_group', 'column_field', 'script_name', 'script_file']
        widgets = {
            'functional_group': forms.Select(attrs={'class': 'form-control'}),
            'column_field': forms.Select(attrs={'class': 'form-control'}),
            'script_name': forms.TextInput(attrs={'class': 'form-control'})
        }
