from django import forms
from django.forms import ModelForm
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
        }


class LabForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(LabForm, self).__init__(*args, **kwargs)
        try:
            tl = FunctionalGroup.objects.get(key='TL')
            self.fields['functional_group'].initial = tl.id
        except FunctionalGroup.DoesNotExist:
            self.fields['functional_group'].initial = None

    class Meta:
        model = LabMetrics
        exclude = ['created', 'confirmed']
        widgets = {
            'functional_group': forms.Select(attrs={
                'class': 'form-control',
                'readonly': True
            })
        }


class RequirementForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RequirementForm, self).__init__(*args, **kwargs)
        try:
            re = FunctionalGroup.objects.get(key='RE')
            self.fields['functional_group'].initial = re.id
        except FunctionalGroup.DoesNotExist:
            self.fields['functional_group'].initial = None

    class Meta:
        model = RequirementMetrics
        exclude = ['created', 'confirmed']
        widgets = {
            'functional_group': forms.Select(attrs={
                'class': 'form-control',
                'readonly': True
            })
        }


class TestForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(TestForm, self).__init__(*args, **kwargs)
    #     try:
    #         pq = FunctionalGroup.objects.get(key='PQ')
    #         self.fields['functional_group'].initial = pq.id
    #     except FunctionalGroup.DoesNotExist:
    #         self.fields['functional_group'].initial = None

    class Meta:
        model = TestMetrics
        exclude = ['created', 'confirmed']
        widgets = {
            'functional_group': forms.Select(attrs={
                'class': 'form-control',
                'readonly': True
            })
        }