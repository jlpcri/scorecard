from django import forms
from django.forms import ModelForm

from models import Automation
from scorecard.apps.users.models import Subteam, HumanResource
from scorecard.apps.personals.models import InnovationStats, LabStats, RequirementStats, TestStats
from scorecard.apps.teams.models import InnovationMetrics, LabMetrics, RequirementMetrics, TestMetrics
from utils import get_model_fields


class AutomationNewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AutomationNewForm, self).__init__(*args, **kwargs)
        level = 'team'
        try:
            abbreviation = kwargs.pop('initial')['abbreviation']
        except KeyError:
            abbreviation = ''
        if abbreviation == 'QE':
            choices = get_model_fields(InnovationMetrics, abbreviation, level=level)
        elif abbreviation == 'TL':
            choices = get_model_fields(LabMetrics, abbreviation, level=level)
        elif abbreviation == 'RE':
            choices = get_model_fields(RequirementMetrics, abbreviation, level=level)
        elif abbreviation in ['QA', 'TE']:
            choices = get_model_fields(TestMetrics, abbreviation, level=level)
        else:
            choices = ''
        self.fields['subteam'] = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                                        queryset=Subteam.objects.filter(parent__abbreviation=abbreviation))
        self.fields['column_field'] = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                                        choices=choices)

    script_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=False)

    class Meta:
        model = Automation
        fields = ['subteam', 'column_field', 'script_name', 'script_file']
        widgets = {
            'subteam': forms.Select(attrs={'class': 'form-control'}),
            'column_field': forms.Select(attrs={'class': 'form-control'}),
            # 'script_name': forms.TextInput(attrs={'class': 'form-control'})
        }


class AutomationPersonalNewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AutomationPersonalNewForm, self).__init__(*args, **kwargs)
        try:
            abbreviation = kwargs.pop('initial')['abbreviation']
        except KeyError:
            abbreviation = ''

        level = 'person'
        if abbreviation == 'QE':
            choices = get_model_fields(InnovationStats, abbreviation, level=level)
        elif abbreviation == 'TL':
            choices = get_model_fields(LabStats, abbreviation, level=level)
        elif abbreviation == 'RE':
            choices = get_model_fields(RequirementStats, abbreviation, level=level)
        elif abbreviation in ['QA', 'TE']:
            choices = get_model_fields(TestStats, abbreviation, level=level)
        else:
            choices = ''
        self.fields['human_resource'] = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                                               queryset=HumanResource.objects.filter(functional_group__abbreviation=abbreviation))
        self.fields['column_field'] = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                                        choices=choices)

    script_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=False)

    class Meta:
        model = Automation
        fields = ['human_resource', 'column_field', 'script_name', 'script_file']
        widgets = {
            'human_resource': forms.Select(attrs={'class': 'form-control'}),
            'column_field': forms.Select(attrs={'class': 'form-control'}),
            # 'script_name': forms.TextInput(attrs={'class': 'form-control'})
        }


class AutomationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AutomationForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['subteam'] = forms.ModelChoiceField(queryset=Subteam.objects.filter(parent__abbreviation=self.instance.subteam.parent.abbreviation),
                                                            widget=forms.Select(attrs={'class': 'form-control',
                                                                                       'readonly': True}))

    script_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=False)

    class Meta:
        model = Automation
        fields = ['subteam', 'column_field', 'script_name', 'script_file']
        widgets = {
            'column_field': forms.TextInput(attrs={'class': 'form-control',
                                                   'readonly': True}),
        }


class AutomationPersonalForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AutomationPersonalForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['human_resource'] = forms.ModelChoiceField(queryset=HumanResource.objects.filter(),
                                                            widget=forms.Select(attrs={'class': 'form-control',
                                                                                       'readonly': True}))

    script_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=False)

    class Meta:
        model = Automation
        fields = ['human_resource', 'column_field', 'script_name', 'script_file']
        widgets = {
            'column_field': forms.TextInput(attrs={'class': 'form-control',
                                                   'readonly': True}),
        }
