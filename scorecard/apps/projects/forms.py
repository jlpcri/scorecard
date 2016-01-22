from django import forms
from django.forms import ModelForm

from models import Project, ProjectPhase, Ticket


class ProjectNewForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class ProjectPhaseNewForm(ModelForm):
    class Meta:
        model = ProjectPhase
        fields = ['project', 'functional_group', 'lead', 'name', 'key']
        widgets = {
            'project': forms.Select(attrs={'class': 'form-control'}),
            'functional_group': forms.Select(attrs={'class': 'form-control'}),
            'lead': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'key': forms.TextInput(attrs={'class': 'form-control', 'required': False})
        }


class TicketNewForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['functional_group', 'lead', 'key']
        widgets = {
            'functional_group': forms.Select(attrs={'class': 'form-control'}),
            'lead': forms.Select(attrs={'class': 'form-control'}),
            'key': forms.TextInput(attrs={'class': 'form-control'})
        }
