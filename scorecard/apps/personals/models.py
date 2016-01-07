from django.db import models
from django.utils.timezone import localtime

from scorecard.apps.users.models import FunctionalGroup, HumanResource


class BaseStats(models.Model):
    """
    Base Individual Status for all teams
    """
    human_resource = models.ForeignKey(HumanResource)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    confirmed = models.DateTimeField(auto_now=True, db_index=True)
    updated = models.BooleanField(default=False)

    # Efficiency
    overtime_weekday = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours
    overtime_weekend = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours
    rework_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours

    class Meta:
        abstract = True
        ordering = ['human_resource__user__first_name']

    def __unicode__(self):
        return '{0}: {1}: {2}'.format(self.human_resource.user.username,
                                      self.human_resource.functional_group.key,
                                      localtime(self.created))


class InnovationStats(BaseStats):
    """
    Personal Performance status for QI team
    """
    # Throughput
    story_points_execution = models.PositiveIntegerField(default=0)
    unit_tests_dev = models.PositiveIntegerField(default=0)
    elicitation_analysis_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours


class LabStats(BaseStats):
    """
    Personal Performance status for TL team
    """
    # Throughput
    tickets_closed = models.PositiveIntegerField(default=0)


class RequirementStats(BaseStats):
    """
    Personal Performance status for RE team
    """
    # Throughput
    elicitation_analysis_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours

    # Quality
    revisions = models.PositiveIntegerField(default=0)

    # Efficiency
    rework_external_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Costs
    travel_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class TestStats(BaseStats):
    """
    Personal Performance status for PQ, QA, TE team
    """
    # Throughput
    tc_manual_dev = models.PositiveIntegerField(default=0)
    tc_manual_dev_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours
    tc_manual_execution = models.PositiveIntegerField(default=0)
    tc_manual_execution_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,)  # in hours
    tc_auto_dev = models.PositiveIntegerField(default=0)
    tc_auto_dev_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours
    tc_auto_execution = models.PositiveIntegerField(default=0)
    tc_auto_execution_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours

    # Quality
    defect_caught = models.PositiveIntegerField(default=0)
    uat_defects_not_prevented = models.PositiveIntegerField(default=0)
    standards_violated = models.PositiveIntegerField(default=0)


