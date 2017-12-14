__author__ = 'sliu'

from django import forms
from .models import RequirementMetrics


class graph_metrics(forms.ModelForm):

    class Meta:
        model = RequirementMetrics
        fields = {'rework_external_time',
                  'creep',
                  'project_loe',
                  'project_actuals',
                  'system_met',
                  'system_miss',
                  'team_initiative',
                  'time_initiatives',
                  }
