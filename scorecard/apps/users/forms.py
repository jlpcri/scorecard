from django import forms
from django.forms import ModelForm
from scorecard.apps.teams.models import RequirementMetrics


class RequirementChartForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RequirementChartForm, self).__init__(*args, **kwargs)
        for field in self.fields:
                self.fields[field] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)


    class Meta:
        model = RequirementMetrics
        # exclude = ['created', 'confirmed', 'updated', 'human_resource', 'elicitation_analysis_time', 'research_time',
        #            'resource_swap_time', 'contractors']
        fields = ['compliments', 'complaints', 'project_loe',
                  'backlog', 'team_initiative', 'time_initiatives', 'active_projects', 'project_actuals',
                  'revisions','srs_initial', 'srs_detail', 'overtime_weekday', 'overtime_weekend', 'rework_time',
                  'rework_external_time', 'pto_holiday_time', 'travel_cost', 'other_savings', 'gap_analysis',
                  'project_time', 'creep', 'system_met', 'system_miss', 'actual_met', 'actual_miss', 'survey'
                  ]