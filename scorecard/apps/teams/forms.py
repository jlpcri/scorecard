from django import forms
from django.forms import ModelForm
from django.shortcuts import redirect, render
from models import TestMetrics, InnovationMetrics, LabMetrics, RequirementMetrics
from scorecard.apps.users.models import FunctionalGroup


class InnovationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(InnovationForm, self).__init__(*args, **kwargs)
        try:
            qi = FunctionalGroup.objects.get(key='QI')
            self.fields['functional_group'].initial = qi.id
        except FunctionalGroup.DoesNotExist:
            self.fields['functional_group'].initial = None

    class Meta:
        model = InnovationMetrics
        exclude = ['created', 'confirmed']
        widgets = {
            'functional_group': forms.Select(attrs={
                'class': 'form-control',
                'readonly': True
            })
            # 'staffs': forms.TextInput(attrs={'class': 'form-control'}),
            # 'openings': forms.TextInput(attrs={'class': 'form-control'}),
            # 'contractors': forms.TextInput(attrs={'class': 'form-control'}),

        }


