from django import forms
from django.forms import ModelForm

from models import Automation, FunctionalGroup
from utils import CHOICES_QE, CHOICES_TL, CHOICES_RE, CHOICES_QA_TE


class AutomationNewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AutomationNewForm, self).__init__(*args, **kwargs)
        try:
            abbreviation = kwargs.pop('initial')['abbreviation']
        except KeyError:
            abbreviation = ''
        if abbreviation == 'QE':
            choices = CHOICES_QE
        elif abbreviation == 'TL':
            choices = CHOICES_TL
        elif abbreviation == 'RE':
            choices = CHOICES_RE
        elif abbreviation in ['QA', 'TE']:
            choices = CHOICES_QA_TE
        else:
            choices = ''
        self.fields['functional_group'] = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                                                 queryset=FunctionalGroup.objects.filter(abbreviation=abbreviation))
        self.fields['column_field'] = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                                        choices=choices)

    script_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=False)

    class Meta:
        model = Automation
        fields = ['functional_group', 'column_field', 'script_name', 'script_file']
        widgets = {
            'functional_group': forms.Select(attrs={'class': 'form-control'}),
            'column_field': forms.Select(attrs={'class': 'form-control'}),
            # 'script_name': forms.TextInput(attrs={'class': 'form-control'})
        }


class AutomationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AutomationForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['functional_group'] = forms.ModelChoiceField(queryset=FunctionalGroup.objects.filter(abbreviation=self.instance.functional_group.abbreviation),
                                                                     widget=forms.Select(attrs={'class': 'form-control',
                                                                                                'readonly': True}))

    script_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=False)

    class Meta:
        model = Automation
        fields = ['functional_group', 'column_field', 'script_name', 'script_file']
        widgets = {
            # 'functional_group': forms.Select(attrs={'class': 'form-control',
            #                                         'readonly': True}),
            'column_field': forms.TextInput(attrs={'class': 'form-control',
                                                   'readonly': True}),
        }
