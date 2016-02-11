from django import forms
from django.forms import ModelForm

from models import Automation
from utils import CHOICES_QI, CHOICES_TL, CHOICES_RE, CHOICES_QA_TE


class AutomationNewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AutomationNewForm, self).__init__(*args, **kwargs)
        key = kwargs.pop('initial')['key']
        if key == 'QI':
            choices = CHOICES_QI
        elif key == 'TL':
            choices = CHOICES_TL
        elif key == 'RE':
            choices = CHOICES_RE
        elif key in ['QA', 'TE']:
            choices = CHOICES_QA_TE
        self.fields['column_field'] = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                                                        choices=choices)

    class Meta:
        model = Automation
        fields = ['functional_group', 'column_field', 'script_name', 'script_file']
        widgets = {
            'functional_group': forms.Select(attrs={'class': 'form-control'}),
            'column_field': forms.Select(attrs={'class': 'form-control'}),
            'script_name': forms.TextInput(attrs={'class': 'form-control'})
        }
