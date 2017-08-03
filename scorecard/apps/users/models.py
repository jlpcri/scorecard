from django.contrib.auth.models import User
from django.db import models
import simplejson

from scorecard.apps.teams.models import TestMetrics, LabMetrics, InnovationMetrics, RequirementMetrics
from scorecard.apps.projects.utils import REVENUE_SCALE_CHOICES


class FunctionalGroup(models.Model):
    """
    Functional Group, such as RE, QA, QI, TL
    """
    TESTING = 'Testing'
    DEVELOPMENT = 'Development'
    REQUIREMENTS = 'Requirements'
    LAB = 'Lab'
    METRIC_CHOICES = (
        ('Testing', TESTING),
        ('Development', DEVELOPMENT),
        ('Requirements', REQUIREMENTS),
        ('Lab', LAB)
    )

    name = models.CharField(max_length=50, unique=True, default='')
    abbreviation = models.CharField(max_length=4, unique=True, default='')
    metric_type = models.CharField(max_length=13, choices=METRIC_CHOICES, default=TESTING)

    def __unicode__(self):
        return '{0}: {1}'.format(self.name, self.abbreviation)

    class Meta:
        verbose_name_plural = "Functional Groups"

    @property
    def metrics_set(self):
        if self.metric_type == self.TESTING:
            return self.testmetrics_set
        elif self.metric_type == self.DEVELOPMENT:
            return self.innovationmetrics_set
        elif self.metric_type == self.REQUIREMENTS:
            return self.requirementmetrics_set
        elif self.metric_type == self.LAB:
            return self.labmetrics_set

    def metric_fields(self):
        metric = self.metrics()
        if not metric:
            return None

        fields = metric._meta.get_fields()

        if self.metric_type == self.TESTING:
            EXCLUSION_LIST = ['id', 'created', 'confirmed', 'functional_group', 'updated', 'subteam']
            return [field for field in fields if field.name not in EXCLUSION_LIST]
        elif self.metric_type == self.DEVELOPMENT:
            EXCLUSION_LIST = ['id', 'created', 'confirmed', 'functional_group', 'updated', 'subteam']
            return [field for field in fields if field.name not in EXCLUSION_LIST]
        elif self.metric_type == self.REQUIREMENTS:
            EXCLUSION_LIST = ['id', 'created', 'confirmed', 'functional_group', 'updated', 'subteam', 'escalations',
                              'slas_met', 'sdis_not_prevented', 'rework_introduced_time', 'resource_swap',
                              'resource_swap_time', 'license_cost', 'slas_missed', 'elicitation_analysis_time']
            return [field for field in fields if field.name not in EXCLUSION_LIST]
        elif self.metric_type == self.LAB:
            EXCLUSION_LIST = ['id', 'created', 'confirmed', 'functional_group', 'updated', 'subteam']
            return [field for field in fields if field.name not in EXCLUSION_LIST]

    def metrics(self):
        if self.metric_type == self.TESTING:
            return TestMetrics.objects.filter(functional_group=self).first()
        elif self.metric_type == self.DEVELOPMENT:
            return InnovationMetrics.objects.filter(functional_group=self).first()
        elif self.metric_type == self.REQUIREMENTS:
            return RequirementMetrics.objects.filter(functional_group=self).first()
        elif self.metric_type == self.LAB:
            return LabMetrics.objects.filter(functional_group=self).first()

    @property
    def quality_graph(self):
        try:
            return self.metrics().quality_graph
        except AttributeError:  # metrics == None, i.e. no data loaded
            # print self.metrics()
            return None

    def efficiency_graph(self):
        try:
            return self.metrics().efficiency_graph()
        except AttributeError:  # metrics == None, i.e. no data loaded
            # print self.metrics()
            return None

    def throughput_graph(self):
        try:
            return self.metrics().throughput_graph()
        except AttributeError:  # metrics == None, i.e. no data loaded
            # print self.metrics()
            return None

    def progress_graph(self):
        try:
            return self.metrics().progress_graph()
        except AttributeError:  # metrics == None, i.e. no data loaded
            # print self.metrics()
            return None

    @property
    def key(self):
        return self.abbreviation if self.abbreviation not in ['BPO', 'QE'] else 'QI'


class Subteam(models.Model):
    """
    Division of a functional group
    """
    parent = models.ForeignKey(FunctionalGroup)
    name = models.TextField()
    hourly_rate = models.IntegerField(default=50)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.parent.abbreviation + " " + self.name

    @property
    def metrics_set(self):
        parent_metric_type = self.parent.metric_type
        if parent_metric_type == self.parent.TESTING:
            return self.testmetrics_set
        elif parent_metric_type == self.parent.DEVELOPMENT:
            return self.innovationmetrics_set
        elif parent_metric_type == self.parent.REQUIREMENTS:
            return self.requirementmetrics_set
        elif parent_metric_type == self.parent.LAB:
            return self.labmetrics_set

    @property
    def gantt_phases(self):
        data = []
        dependencies = ''
        for item in self.projectphase_set.all():
            if not item.actual_end:
                for scale in REVENUE_SCALE_CHOICES:
                    if item.project.revenue_scale == scale[0]:
                        dependencies = scale[1]

                data.append({
                    'id': 'phase_' + str(item.id),
                    'name': item.project.name + ': ' + item.name,
                    'resource': 'Workers: ' + str(item.worker.count()) + ', Revenue: ' + dependencies,
                    'start': item.estimate_start.strftime('%Y-%m-%d') if item.estimate_start else None,
                    'end': item.estimate_end.strftime('%Y-%m-%d') if item.estimate_end else None,
                    'duration': None,
                    'percent_complete': None,
                    'dependencies': None
                })

        return data

    @property
    def gantt_tickets(self):
        data = []
        dependencies = ''
        for item in self.ticket_set.all():
            if not item.actual_end:
                for scale in REVENUE_SCALE_CHOICES:
                    if item.revenue_scale == scale[0]:
                        dependencies = scale[1]
                data.append({
                    'id': 'ticket_' + str(item.id),
                    'name': 'Ticket: ' + item.key,
                    'resource': 'Workers: ' + str(item.worker.count()) + ', Revenue: ' + dependencies,
                    'start': item.estimate_start.strftime('%Y-%m-%d') if item.estimate_start else None,
                    'end': item.estimate_end.strftime('%Y-%m-%d') if item.estimate_end else None,
                    'duration': None,
                    'percent_complete': None,
                    'dependencies': None
                })

        return data

    @property
    def gantt_chart_data(self):
        return self.gantt_phases + self.gantt_tickets


class HumanResource(models.Model):
    """
    Link to auth user
    """
    functional_group = models.ForeignKey(FunctionalGroup, null=True, blank=True)
    subteam = models.ForeignKey(Subteam, null=True, blank=True)
    user = models.OneToOneField(User)

    manager = models.BooleanField(default=False)
    contractor = models.BooleanField(default=False)

    def __unicode__(self):
        if self.functional_group:
            return '{0} {1}: {2}'.format(self.user.first_name,
                                          self.user.last_name,
                                          self.functional_group.abbreviation)
        else:
            return '{0}: {1}'.format(self.user.username, 'No Team')

    @property
    def stat_set(self):
        if self.functional_group.metric_type == FunctionalGroup.TESTING:
            return self.teststats_set
        elif self.functional_group.metric_type == FunctionalGroup.REQUIREMENTS:
            return self.requirementstats_set
        elif self.functional_group.metric_type == FunctionalGroup.DEVELOPMENT:
            return self.innovationstats_set
        elif self.functional_group.metric_type == FunctionalGroup.LAB:
            return self.labstats_set

    class Meta:
        ordering = ['user__last_name', ]


class ColumnPreference(models.Model):
    user = models.ForeignKey(User)

    # this is name of the table that will have rows that can be shown or hidden
    table_name = models.CharField(default='', max_length=50, blank=False)

    # this is a comma delimited list of columns the user wants to hide
    hide_list = models.CharField(default='', max_length=750, blank=True)

    def __unicode__(self):
        return str(self.user.username) + "  " + self.table_name + "  " + str(self.hide_list)

    class Meta:
        ordering = ('user',)
        verbose_name = "Column Preference"

    def unpack(self):
        return simplejson.dumps(self.hide_list) if self.hide_list else []


