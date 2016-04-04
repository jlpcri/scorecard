from django import forms
from django.forms import ModelForm
from models import TestMetrics, InnovationMetrics, LabMetrics, RequirementMetrics


class InnovationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(InnovationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field in ['elicitation_analysis_time',
                         'rework_introduced_time',
                         'overtime_weekday', 'overtime_weekend', 'rework_time', 'resource_swap_time',
                         'license_cost', 'other_savings',
                         ]:
                self.fields[field] = forms.DecimalField(widget=forms.NumberInput(attrs={'min': '0'}))
            elif field in ['unit_tests_coverage', 'documentation_coverage', 'slas_met']:
                self.fields[field] = forms.DecimalField(widget=forms.NumberInput(attrs={'min': '0',
                                                                                        'max': '1',
                                                                                        'step': '0.05',
                                                                                        'style': 'width: 100%'}))

    class Meta:
        model = InnovationMetrics
        exclude = ['created', 'confirmed', 'updated', 'functional_group', 'sdis_not_prevented']


class LabForm(ModelForm):
    class Meta:
        model = LabMetrics
        fields = ['staffs', 'openings', 'contractors', 'compliments', 'complaints',
                  'tickets_received', 'tickets_closed', 'virtual_machines', 'physical_machines', 'monitor_machines',
                  'builds_submitted', 'builds_accepted', 'platform_drift_violations', 'updates_install_docs',
                  'administration_time', 'project_time', 'ticket_time', 'slas_met', 'pto_holiday_time',
                  'power_consumption_ups_a', 'power_consumption_ups_b', 'license_cost', 'other_savings'
                  ]


class RequirementForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RequirementForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field in ['elicitation_analysis_time',
                         'slas_missed', 'rework_introduced_time',
                         'overtime_weekday', 'overtime_weekend', 'rework_external_time', 'resource_swap_time',
                         'travel_cost'
                         ]:
                self.fields[field] = forms.DecimalField(widget=forms.NumberInput(attrs={'min': '0'}))

        self.fields['slas_met'] = forms.DecimalField(widget=forms.NumberInput(attrs={'min': '0',
                                                                                     'max': '1',
                                                                                     'step': '0.05',
                                                                                     'style': 'width: 100%'}))

    class Meta:
        model = RequirementMetrics
        fields = ['staffs', 'openings', 'contractors', 'compliments', 'complaints',
                  'backlog', 'team_initiative', 'active_projects', 'elicitation_analysis_time',
                  'revisions', 'rework_introduced_time', 'slas_met', 'slas_missed', 'escalations',
                  'overtime_weekday', 'overtime_weekend', 'rework_external_time', 'pto_holiday_time',
                  'travel_cost', 'other_savings'
                  ]


class TestForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field in ['rework_introduced_time',
                         'overtime_weekday', 'overtime_weekend', 'rework_time', 'resource_swap_time',
                         'license_cost', 'other_savings',
                         'tc_manual_dev_time', 'tc_manual_execution_time',
                         'tc_auto_dev_time', 'tc_auto_execution_time',
                         ]:
                self.fields[field] = forms.DecimalField(widget=forms.NumberInput(attrs={'min': '0'}))

        self.fields['slas_met'] = forms.DecimalField(widget=forms.NumberInput(attrs={'min': '0',
                                                                                     'max': '1',
                                                                                     'step': '0.05',
                                                                                     'style': 'width: 100%'}))

    class Meta:
        model = TestMetrics
        exclude = ['created', 'confirmed', 'updated', 'functional_group']
        # widgets = {
        #     'functional_group': forms.Select(attrs={
        #         'class': 'form-control',
        #         'readonly': True
        #     })
        # }
