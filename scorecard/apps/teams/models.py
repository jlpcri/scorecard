from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.timezone import localtime

from scorecard.apps.users.models import FunctionalGroup


class BaseMetrics(models.Model):
    """
    Base Metrics for all four different metrics
    """
    functional_group = models.ForeignKey(FunctionalGroup)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    confirmed = models.DateTimeField(auto_now=True, db_index=True)

    # Human Resource
    staffs = models.IntegerField(default=0)
    contractors = models.IntegerField(default=0)
    openings = models.IntegerField(default=0)

    # Quality
    slas_met = models.DecimalField(max_digits=3, decimal_places=2, default=0,
                                   validators=[MaxValueValidator(1)])
    delays_introduced_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours
    sdis_not_prevented = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    resource_swap = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    escalations = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    rework_introduced_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours

    # Efficiency
    avg_team_size = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    overtime_weekday = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours
    overtime_weekend = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours
    rework_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours
    resource_swap_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours

    # Costs
    license_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    other_savings = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        abstract = True


class TestMetrics(BaseMetrics):
    """
    Metrics for groups: Quality Assurance, Test Engineering, Product Quality
    """
    # Throughput
    team_initiative = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ticket_backlog = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ticket_prep = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ticket_execution = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ticket_closed = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    project_backlog = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    project_prep = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    project_execution = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    project_closed = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tc_manual_dev = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tc_manual_dev_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours
    tc_manual_execution = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tc_manual_execution_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours
    tc_auto_dev = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tc_auto_dev_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours
    tc_auto_execution = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tc_auto_execution_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours

    # Quality
    defect_caught = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    uat_defects_not_prevented = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Efficiency
    avg_time_frame = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Costs

    def __unicode__(self):
        return '{0}: {1}: {2}'.format(self.functional_group.name,
                                      localtime(self.confirmed),
                                      localtime(self.created))

    @property
    def auto_footprint_dev_age(self):
        if self.tc_manual_dev + self.tc_auto_dev == 0:
            return self.tc_auto_dev
        else:
            return self.tc_auto_dev / (self.tc_manual_dev + self.tc_auto_dev)

    @property
    def auto_footprint_execution_age(self):
        if self.tc_manual_execution + self.tc_auto_execution == 0:
            return self.tc_auto_execution
        else:
            return self.tc_auto_execution / (self.tc_manual_execution + self.tc_auto_execution)

    @property
    def avg_throughput(self):
        dev = self.tc_manual_dev + self.tc_auto_dev
        execution = self.tc_manual_execution + self.tc_auto_execution
        hrs = self.staffs + self.contractors
        if hrs == 0:
            return 0
        else:
            return (dev + execution) / hrs

    @property
    def active_projects(self):
        return self.project_prep + self.project_execution

    @property
    def active_tickets(self):
        return self.ticket_prep + self.ticket_execution

    @property
    def auto_and_execution_time(self):
        return self.tc_manual_dev_time\
               + self.tc_manual_execution_time\
               + self.tc_auto_dev_time\
               + self.tc_auto_execution_time

    @property
    def gross_available_time(self):
        return (self.staffs + self.contractors) * 30

    @property
    def efficiency(self):
        if self.gross_available_time == 0:
            return 0
        else:
            return self.auto_and_execution_time / self.gross_available_time

    @property
    def operational_cost(self):
        """
        Different computer formula for Product Quality, Quality Assrance, and Test Engineering
        """
        if self.functional_group.key == 'PQ':
            return (self.staffs + self.contractors) * 30 * 60
        elif self.functional_group.key == 'QA':
            return self.staffs * 40 * 40 + self.contractors * 100 * 40
        elif self.functional_group.key == 'TE':
            return self.staffs * 40 * 50
        else:
            return 0

    @property
    def total_operational_cost(self):
        return self.operational_cost + self.license_cost

    @property
    def auto_savings(self):
        """
        Cost Saved by Automation
        """
        if self.functional_group.key == 'PQ':
            return self.tc_auto_execution_time * 40
        elif self.functional_group.key == 'QA':
            return self.tc_auto_execution_time * 40
        elif self.functional_group.key == 'TE':
            return (self.tc_auto_execution_time + 37) * 50
        else:
            return 0


class InnovationMetrics(BaseMetrics):
    """
    Metrics for group: Quality Innovation
    """

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
    elicitation_analysis_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours
    revisions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    active_projects = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Quality
    uat_defects_not_prevented = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Usage
    pheme_manual_tests = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    pheme_auto_tests = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    visilog_txl_parsed = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    visilog_txl_schema_violation = models.DecimalField(max_digits=19, decimal_places=2, default=0)

    def __unicode__(self):
        return '{0}: {1}: {2}'.format(self.functional_group.name,
                                      localtime(self.confirmed),
                                      localtime(self.created))

    @property
    def operational_cost(self):
        # 40 (hours per week) * 45(hourly rate)
        return (self.staffs + self.contractors) * 40 * 45

    @property
    def total_operational_cost(self):
        return self.operational_cost + self.license_cost


class RequirementMetrics(BaseMetrics):
    """
    Metrics for group: Requirements Engineering
    """

    # Throughput
    backlog = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    team_initiative = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    active_projects = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    elicitation_analysis_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours

    # Quality
    revisions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    slas_missed = models.DecimalField(max_digits=3, decimal_places=2, default=0,
                                      validators=[MaxValueValidator(1)])

    # Efficiency
    rework_external_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Costs
    travel_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __unicode__(self):
        return '{0}: {1}: {2}'.format(self.functional_group.name,
                                      localtime(self.confirmed),
                                      localtime(self.created))

    @property
    def avg_throughput(self):
        return self.active_projects + self.team_initiative

    @property
    def gross_available_time(self):
        return self.staffs * 6 * 5

    @property
    def efficiency(self):
        if self.gross_available_time == 0:
            return 0
        else:
            return self.elicitation_analysis_time / self.gross_available_time

    @property
    def rework_external_cost(self):
        return self.rework_external_time * 50

    @property
    def operational_cost(self):
        return (self.staffs + self.contractors) * 30 * 50

    @property
    def total_operational_cost(self):
        return self.operational_cost + self.license_cost

    @property
    def overall_cost(self):
        return self.total_operational_cost + self.travel_cost


class LabMetrics(BaseMetrics):
    """
    Metrics for group: Test Lab
    """
    # Throughput
    tickets_received = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tickets_closed = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    virtual_machines = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    physical_machines = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # Costs
    power_consumption_ups_a = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in kw
    power_consumption_ups_b = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in kw

    def __unicode__(self):
        return '{0}: {1}: {2}'.format(self.functional_group.name,
                                      localtime(self.confirmed),
                                      localtime(self.created))

    @property
    def total_operational_cost(self):
        return self.power_consumption_ups_a + self.power_consumption_ups_b + self.license_cost


