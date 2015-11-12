from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.timezone import localtime

from scorecard.apps.users.models import FunctionalGroup


class TestingMetrics(models.Model):
    """
    Metrics for groups: Quality Assurance, Testing Engineering, Product Quality
    """
    functional_group = models.ForeignKey(FunctionalGroup)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    confirmed = models.DateTimeField(auto_now=True, db_index=True)

    # Human Resource
    staffs = models.IntegerField(default=0)
    contractors = models.IntegerField(default=0)
    openings = models.IntegerField(default=0)

    # Throughput

    # Quality

    # Efficiency

    # Costs


class InnovationMetrics(models.Model):
    """
    Metrics for group: Quality Innovation
    """
    functional_group = models.ForeignKey(FunctionalGroup)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    confirmed = models.DateTimeField(auto_now=True, db_index=True)

    # Human Resource
    staffs = models.IntegerField(default=0)
    contractors = models.IntegerField(default=0)
    openings = models.IntegerField(default=0)

    # Throughput
    story_points_backlog = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    story_points_prep = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    story_points_execution = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unit_tests_dev = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unit_tests_coverage = models.DecimalField(max_digits=3, decimal_places=2, default=0,
                                              validators=[MaxValueValidator(1)])
    documentation_coverage = models.DecimalField(max_digits=3, decimal_places=2, default=0,
                                                 validators=[MaxValueValidator(1)])
    defects_in_dev = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    elicitation_analysis_hours = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    revisions = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Quality
    slas_met = models.DecimalField(max_digits=3, decimal_places=2, default=0,
                                   validators=[MaxValueValidator(1)])
    delays_introduced_hours = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    uat_defects_not_prevented = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sdis_not_prevented = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    resource_swap = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    escalations = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    rework_introduced_hours = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Efficiency
    overtime_weekday_hours = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    overtime_weekend_hours = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    rework_hours = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    resource_swap_hours = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Costs
    code_operational_cost = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    license_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Usage
    pheme_manual_tests = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    pheme_auto_tests = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    visilog_txl_parsed = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    visilog_txl_schema_violation = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    other_savings = models.DecimalField(max_digits=19, decimal_places=2, default=0)

    def __unicode__(self):
        return '{0}: {1}: {2}'.format(self.functional_group.name,
                                      localtime(self.confirmed),
                                      localtime(self.created))

    @property
    def average_team_size(self):
        return 0

    @property
    def total_operational_cost(self):
        return self.code_operational_cost + self.license_cost


class RequirementsMetrics(models.Model):
    """
    Metrics for group: Requirements Engineering
    """
    functional_group = models.ForeignKey(FunctionalGroup)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    confirmed = models.DateTimeField(auto_now=True, db_index=True)

    # Human Resource
    staffs = models.IntegerField(default=0)
    contractors = models.IntegerField(default=0)
    openings = models.IntegerField(default=0)

    # Throughput

    # Quality

    # Efficiency

    # Costs


class LabMetrics(models.Model):
    """
    Metrics for group: Testing Lab
    """
    functional_group = models.ForeignKey(FunctionalGroup)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    confirmed = models.DateTimeField(auto_now=True, db_index=True)

    # Human Resource
    staffs = models.IntegerField(default=0)
    contractors = models.IntegerField(default=0)
    openings = models.IntegerField(default=0)

    # Throughput

    # Quality

    # Efficiency

    # Costs

