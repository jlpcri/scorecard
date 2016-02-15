from django import forms
from django.forms import ModelForm

from models import Automation, FunctionalGroup
from utils import CHOICES_QI, CHOICES_TL, CHOICES_RE, CHOICES_QA_TE


class AutomationNewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AutomationNewForm, self).__init__(*args, **kwargs)
        try:
            key = kwargs.pop('initial')['key']
        except KeyError:
            key = ''
        if key == 'QI':
            choices = CHOICES_QI
        elif key == 'TL':
            choices = CHOICES_TL
        elif key == 'RE':
            choices = CHOICES_RE
        elif key in ['QA', 'TE']:
            choices = CHOICES_QA_TE
        else:
            choices = ''
        self.fields['functional_group'] = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                                                 queryset=FunctionalGroup.objects.filter(key=key))
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
            self.fields['functional_group'] = forms.ModelChoiceField(queryset=FunctionalGroup.objects.filter(key=self.instance.functional_group.key),
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
