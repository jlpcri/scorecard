from django.contrib.auth.models import User
from django.db import models

import simplejson

from scorecard.apps.teams.models import TestMetrics, LabMetrics, InnovationMetrics, RequirementMetrics


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
    abbreviation = models.CharField(max_length=4, unique=True, default = '')
    metric_type = models.CharField(max_length=13, choices=METRIC_CHOICES, default=TESTING)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Functional Groups"

    @property
    def metrics_set(self):
        if self.metric_type == self.TESTING:
            return self.testmetrics_set.order_by('-created')
        elif self.metric_type == self.DEVELOPMENT:
            return self.innovationmetrics_set.order_by('-created')
        elif self.metric_type == self.REQUIREMENTS:
            return self.requirementmetrics_set.order_by('-created')
        elif self.metric_type == self.LAB:
            return self.labmetrics_set.order_by('-created')

    def metric_fields(self):
        if self.metric_type == self.TESTING:
            metric = TestMetrics
        elif self.metric_type == self.DEVELOPMENT:
            metric = InnovationMetrics
        elif self.metric_type == self.REQUIREMENTS:
            metric = RequirementMetrics
        elif self.metric_type == self.LAB:
            metric = LabMetrics

        fields = metric._meta.get_fields()
        EXCLUSION_LIST = ['id', 'created', 'confirmed', 'functional_group', 'updated']
        return [field for field in fields if field.name not in EXCLUSION_LIST]


class Subteam(models.Model):
    """
    Division of a functional group
    """
    parent = models.ForeignKey(FunctionalGroup)
    name = models.TextField()
    hourly_rate = models.IntegerField(default=50)


class HumanResource(models.Model):
    """
    Link to auth user
    """
    functional_group = models.ForeignKey(FunctionalGroup, null=True, blank=True)
    user = models.OneToOneField(User)

    manager = models.BooleanField(default=False)
    contractor = models.BooleanField(default=False)

    def __unicode__(self):
        if self.functional_group:
            return '{0}: {1}: {2}'.format(self.user.username,
                                          self.functional_group.abbreviation,
                                          self.manager)
        else:
            return '{0}: {1}: {2}'.format(self.user.username, 'No Team',  self.manager)

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


