from django import forms
from django.forms import ModelForm
from models import TestMetrics, InnovationMetrics, LabMetrics, RequirementMetrics


class InnovationForm(ModelForm):
    class Meta:
        model = InnovationMetrics
        exclude = ['created', 'confirmed', 'updated']
        widgets = {
            'functional_group': forms.Select(attrs={
                'class': 'form-control',
                'readonly': True
            })
        }


class LabForm(ModelForm):
    class Meta:
        model = LabMetrics
        fields = ['functional_group', 'staffs', 'openings', 'contractors',
                  'tickets_received', 'tickets_closed', 'virtual_machines', 'physical_machines',
                  'power_consumption_ups_a', 'power_consumption_ups_b', 'license_cost'
                  ]
        widgets = {
            'functional_group': forms.Select(attrs={
                'class': 'form-control',
                'readonly': True
            })
        }


class RequirementForm(ModelForm):
    class Meta:
        model = RequirementMetrics
        fields = ['functional_group', 'staffs', 'openings', 'contractors',
                  'backlog', 'team_initiative', 'active_projects', 'elicitation_analysis_time',
                  'revisions', 'rework_introduced_time', 'slas_met', 'slas_missed', 'delays_introduced_time', 'escalations',
                  'overtime_weekday', 'overtime_weekend', 'rework_external_time',
                  'travel_cost'
                  ]
        widgets = {
            'functional_group': forms.Select(attrs={
                'class': 'form-control',
                'readonly': True
            })
        }


class TestForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(TestForm, self).__init__(*args, **kwargs)
    #     for field in self.fields:
    #         if field not in ['functional_group', 'staffs', 'openings', 'contractors']:
    #             self.fields[field] = forms.DecimalField(widget=forms.TextInput())

    class Meta:
        model = TestMetrics
        exclude = ['created', 'confirmed', 'updated']
        widgets = {
            'functional_group': forms.Select(attrs={
                'class': 'form-control',
                'readonly': True
            })
        }
