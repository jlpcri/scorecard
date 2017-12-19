from django import forms
from django.forms import ModelForm

from scorecard.apps.teams.models import RequirementMetrics, TeamGraph


class TeamGraphForm(ModelForm):
    class Meta:
        model = TeamGraph
        fields = ['graph_name', 'selections', 'position']
