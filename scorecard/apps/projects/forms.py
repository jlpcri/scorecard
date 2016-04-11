from django import forms
from django.forms import ModelForm

from models import Project, ProjectPhase, Ticket


class ProjectNewForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'revenue_scale']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'revenue_scale': forms.Select(attrs={'class': 'form-control'})
        }


class ProjectPhaseNewForm(ModelForm):
    class Meta:
        model = ProjectPhase
        fields = ['project', 'functional_group', 'subteam', 'lead', 'worker', 'name', 'key']
        widgets = {
            'project': forms.Select(attrs={'class': 'form-control'}),
            'functional_group': forms.Select(attrs={'class': 'form-control'}),
            'subteam': forms.Select(attrs={'class': 'form-control'}),
            'lead': forms.Select(attrs={'class': 'form-control'}),
            'worker': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'key': forms.TextInput(attrs={'class': 'form-control', 'required': False})
        }


class TicketNewForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['functional_group', 'subteam', 'revenue_scale', 'lead', 'worker', 'key']
        widgets = {
            'functional_group': forms.Select(attrs={'class': 'form-control'}),
            'subteam': forms.Select(attrs={'class': 'form-control'}),
            'revenue_scale': forms.Select(attrs={'class': 'form-control'}),
            'lead': forms.Select(attrs={'class': 'form-control'}),
            'worker': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'key': forms.TextInput(attrs={'class': 'form-control'})
        }
