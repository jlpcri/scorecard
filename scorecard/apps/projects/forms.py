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
        fields = ['key']
        widgets = {
            'key': forms.TextInput(attrs={'class': 'form-control'})
        }