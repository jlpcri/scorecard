from django import forms
from django.forms import ModelForm

from models import Project, ProjectPhase, Ticket


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
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


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = []
        widgets = {
            'functional_group': forms.Select(attrs={'class': 'form-control'}),
            'lead': forms.Select(attrs={'class': 'form-control'}),
            'key': forms.TextInput(attrs={'class': 'form-control'})
        }