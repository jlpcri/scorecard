from django.db import models
from django.utils.timezone import localtime

from scorecard.apps.users.models import FunctionalGroup


class BaseMetrics(models.Model):
    """
    Base Metrics for all four different metrics
    """
    functional_group = models.ForeignKey(FunctionalGroup)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    confirmed = models.DateTimeField(auto_now=True, db_index=True)
    updated = models.BooleanField(default=False)

    # Human Resource
    staffs = models.PositiveIntegerField(default=0)
    contractors = models.PositiveIntegerField(default=0)
    openings = models.PositiveIntegerField(default=0)

    # Quality
    slas_met = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    delays_introduced_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours
    sdis_not_prevented = models.PositiveIntegerField(default=0)
    resource_swap = models.PositiveIntegerField(default=0)
    escalations = models.PositiveIntegerField(default=0)
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
    team_initiative = models.PositiveIntegerField(default=0)
    ticket_backlog = models.PositiveIntegerField(default=0)
    ticket_prep = models.PositiveIntegerField(default=0)
    ticket_execution = models.PositiveIntegerField(default=0)
    ticket_closed = models.PositiveIntegerField(default=0)
    project_backlog = models.PositiveIntegerField(default=0)
    project_prep = models.PositiveIntegerField(default=0)
    project_execution = models.PositiveIntegerField(default=0)
    project_closed = models.PositiveIntegerField(default=0)
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
            return self.staffs * 40 * 60 + self.contractors * 40 * 100
        elif self.functional_group.key == 'QA':
            return self.staffs * 40 * 40 + self.contractors * 40 * 100
        elif self.functional_group.key == 'TE':
            return self.staffs * 40 * 50 + self.contractors * 40 * 100
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
            return self.tc_auto_execution_time * 60
        elif self.functional_group.key == 'QA':
            return self.tc_auto_execution_time * 40
        elif self.functional_group.key == 'TE':
            return self.tc_auto_execution_time * 50
        else:
            return 0


class InnovationMetrics(BaseMetrics):
    """
    Metrics for group: Quality Innovation
    """

    # Throughput
    story_points_backlog = models.PositiveIntegerField(default=0)
    story_points_prep = models.PositiveIntegerField(default=0)
    story_points_execution = models.PositiveIntegerField(default=0)
    unit_tests_dev = models.PositiveIntegerField(default=0)
    unit_tests_coverage = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    documentation_coverage = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    defects_in_dev = models.PositiveIntegerField(default=0)
    elicitation_analysis_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours
    revisions = models.PositiveIntegerField(default=0)
    active_projects = models.PositiveIntegerField(default=0)

    # Quality
    uat_defects_not_prevented = models.PositiveIntegerField(default=0)

    # Usage
    pheme_manual_tests = models.PositiveIntegerField(default=0)
    pheme_auto_tests = models.PositiveIntegerField(default=0)
    visilog_txl_parsed = models.PositiveIntegerField(default=0)
    visilog_txl_schema_violation = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return '{0}: {1}: {2}'.format(self.functional_group.name,
                                      localtime(self.confirmed),
                                      localtime(self.created))

    @property
    def avg_throughput(self):
        if self.staffs == 0:
            return 0
        else:
            return self.story_points_execution / self.staffs

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
    backlog = models.PositiveIntegerField(default=0)
    team_initiative = models.PositiveIntegerField(default=0)
    active_projects = models.PositiveIntegerField(default=0)
    elicitation_analysis_time = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # in hours

    # Quality
    revisions = models.PositiveIntegerField(default=0)
    slas_missed = models.DecimalField(max_digits=3, decimal_places=2, default=0)

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
    tickets_received = models.PositiveIntegerField(default=0)
    tickets_closed = models.PositiveIntegerField(default=0)
    virtual_machines = models.PositiveIntegerField(default=0)
    physical_machines = models.PositiveIntegerField(default=0)

    # Costs
    power_consumption_ups_a = models.PositiveIntegerField(default=0)  # in kw
    power_consumption_ups_b = models.PositiveIntegerField(default=0)  # in kw

    def __unicode__(self):
        return '{0}: {1}: {2}'.format(self.functional_group.name,
                                      localtime(self.confirmed),
                                      localtime(self.created))
