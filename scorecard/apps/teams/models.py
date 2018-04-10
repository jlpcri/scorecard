from __future__ import division

from decimal import Decimal
from django.db import models
from django.utils.timezone import localtime
from django.core.validators import MinValueValidator


class BaseMetrics(models.Model):
    """
    Base Metrics for all four different metrics
    """
    functional_group = models.ForeignKey('users.FunctionalGroup', blank=True, null=True)
    subteam = models.ForeignKey('users.Subteam', blank=True, null=True)
    created = models.DateTimeField(db_index=True)
    confirmed = models.DateTimeField(auto_now=True, db_index=True)
    updated = models.BooleanField(default=False)

    # Human Resource
    staffs = models.PositiveIntegerField(default=0, verbose_name='Staff')
    contractors = models.PositiveIntegerField(default=0, verbose_name='Contractor')
    openings = models.PositiveIntegerField(default=0, verbose_name='Opening')

    # Awards and Punish
    compliments = models.PositiveIntegerField(default=0, verbose_name='Compliment')
    complaints = models.PositiveIntegerField(default=0, verbose_name='Complaint')
    escalations = models.PositiveIntegerField(default=0, verbose_name='Escalation')

    # Quality
    slas_met = models.DecimalField(max_digits=3, decimal_places=2, default=0, verbose_name='SLAs Met')
    sdis_not_prevented = models.PositiveIntegerField(default=0, verbose_name='SDIs not Prevented')
    resource_swap = models.PositiveIntegerField(default=0, verbose_name='Resource Swap')
    rework_introduced_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                                 verbose_name='Rework Introduced Time')  # in hours

    # Efficiency
    overtime_weekday = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                           verbose_name='Overtime Weekday')
    overtime_weekend = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                           verbose_name='Overtime Weekend')
    rework_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                      verbose_name='Rework Time')  # in hours
    resource_swap_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                             verbose_name='Resource Swap Time')  # in hours
    pto_holiday_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                           validators=[MinValueValidator(Decimal(0))],
                                           verbose_name='PTO/Holiday Time')  # in hours

    # Costs
    license_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                       verbose_name='License Cost')
    other_savings = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                        verbose_name='Other Saving')

    class Meta:
        abstract = True

    def __unicode__(self):
        return '{0}: {1}: {2}'.format(self.functional_group.name,
                                      localtime(self.confirmed),
                                      localtime(self.created))

    def table_row(self):
        fields = self.functional_group.metric_fields()
        return [self.__dict__[field.name] for field in fields]


class TestMetrics(BaseMetrics):
    """
    Metrics for groups: Quality Assurance, Test Engineering, Product Quality
    """
    # Human Resource
    testers = models.PositiveIntegerField(default=0, verbose_name='tester')

    # Throughput
    team_initiative = models.PositiveIntegerField(default=0, verbose_name='Team Initiative')
    ticket_backlog = models.PositiveIntegerField(default=0, verbose_name='Ticket Backlog')
    ticket_prep = models.PositiveIntegerField(default=0, verbose_name='Ticket Prep')
    ticket_execution = models.PositiveIntegerField(default=0, verbose_name='Ticket Exec')
    ticket_closed = models.PositiveIntegerField(default=0, verbose_name='Ticket Closed')
    project_backlog = models.PositiveIntegerField(default=0, verbose_name='Project Backlog')
    project_prep = models.PositiveIntegerField(default=0, verbose_name='Project Prep')
    project_execution = models.PositiveIntegerField(default=0, verbose_name='Project Exec')
    project_closed = models.PositiveIntegerField(default=0, verbose_name='Project Closed')
    tc_manual_dev = models.PositiveIntegerField(default=0, verbose_name='TC Manually Dev')
    tc_manual_dev_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                             verbose_name='TC Manually Dev Time')
    tc_manual_execution = models.PositiveIntegerField(default=0, verbose_name='TC Manually Exec')
    tc_manual_execution_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                                   verbose_name='TC Manually Exec Time')
    tc_auto_dev = models.PositiveIntegerField(default=0, verbose_name='TC Auto Dev')
    tc_auto_dev_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                           verbose_name='TC Auto Dev Time')
    tc_auto_execution = models.PositiveIntegerField(default=0, verbose_name='TC Auto Exec')
    tc_auto_execution_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                                 verbose_name='TC Auto Exec Time')
    estimate_auto_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                             validators=[MinValueValidator(Decimal(0))],
                                             verbose_name='Estimated manual time for automation')
    standard_work_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                             validators=[MinValueValidator(Decimal(0))],
                                             verbose_name='Standard Work Time')  #  hours spent doing test documentation and associated overhead
    initiative_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                          validators=[MinValueValidator(Decimal(0))],
                                          verbose_name='Initiatives Time')  # in hours

    # Quality
    defect_caught = models.PositiveIntegerField(default=0, verbose_name='Eefects Caught')
    uat_defects_not_prevented = models.PositiveIntegerField(default=0, verbose_name='UAT Defects not Prevented')
    standards_violated = models.PositiveIntegerField(default=0, verbose_name='Standards Violated')

    # Efficiency
    loe_deviation = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                        verbose_name='LOE Deviation Time')  # in hours

    # Costs

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
    def productive_hours(self):
        return self.auto_and_execution_time + self.standard_work_time

    @property
    def gross_available_time(self):
        return self.testers * 30

    @property
    def utilization(self):
        if (self.testers * 40 - self.pto_holiday_time) != 0:
            return (self.productive_hours + self.initiative_time) / (self.testers * 40 - self.pto_holiday_time)
        else:
            return 0

    @property
    def efficiency(self):
        if self.gross_available_time == 0:
            return 0
        else:
            return self.auto_and_execution_time / self.gross_available_time

    @property
    def operational_cost(self):
        """
        Different computer formula for Product Quality, Quality Assurance, and Test Engineering
        """
        try:
            test_metric_config = TestMetricsConfiguration.objects.get(functional_group__abbreviation=self.functional_group.abbreviation)
            hours = test_metric_config.hours_per_week
            costs_staff = test_metric_config.costs_per_hour_staff
            costs_contractor = test_metric_config.costs_per_hour_contractor
        except TestMetricsConfiguration.DoesNotExist:
            hours, costs_staff, costs_contractor = 0, 0, 0

        return self.staffs * hours * costs_staff + self.contractors * hours * costs_contractor

    @property
    def total_operational_cost(self):
        return self.operational_cost + self.license_cost

    @property
    def auto_savings(self):
        """
        Cost Saved by Automation
        """
        try:
            test_metric_config = TestMetricsConfiguration.objects.get(functional_group__abbreviation=self.functional_group.abbreviation)
            costs_staff = test_metric_config.costs_per_hour_staff
        except TestMetricsConfiguration.DoesNotExist:
            costs_staff = 0

        return (self.estimate_auto_time - self.tc_auto_execution_time) * costs_staff

    def quality_graph(self):
        data = self.functional_group.testmetrics_set.filter(subteam=None).order_by("-created")[:12]
        return {'title': 'UAT Defects',
                'data': [{'date': week.created.strftime("%b %-d"), 'value': week.uat_defects_not_prevented} for week in data]}

    def efficiency_graph(self):
        data = self.functional_group.testmetrics_set.filter(subteam=None).order_by("-created")[:12]
        return {'title': 'Average Throughput',
                'data': [{'date': week.created.strftime("%b %-d"), 'value': week.avg_throughput} for week in data]}

    def throughput_graph(self):
        data = self.functional_group.testmetrics_set.filter(subteam=None).order_by("-created")[:12]
        return {'title': 'Defects Found',
                'data': [{'date': week.created.strftime("%b %-d"), 'value': week.defect_caught} for week in data]}

    def progress_graph(self):
        data = self.functional_group.testmetrics_set.filter(updated=True, subteam=None).order_by("-created")[:4]
        automatic = sum([week.tc_auto_execution for week in data])
        manual = sum([week.tc_manual_execution for week in data])
        return {'title': 'Test Case Automation',
                'data': {'positive': {'value': automatic, 'label': 'Automatic'},
                         'negative': {'value': manual, 'label': 'Manual'}}}

    class Meta:
        verbose_name_plural = "Test Metrics"


class InnovationMetrics(BaseMetrics):
    """
    Metrics for group: Quality Innovation
    """

    # Throughput
    story_points_backlog = models.PositiveIntegerField(default=0, verbose_name='Story Points Backlog')
    story_points_prep = models.PositiveIntegerField(default=0, verbose_name='Story Points Prep')
    story_points_execution = models.PositiveIntegerField(default=0, verbose_name='Story Points Exec')
    unit_tests_dev = models.PositiveIntegerField(default=0, verbose_name='Unit Tests Dev')
    unit_tests_coverage = models.DecimalField(max_digits=3, decimal_places=2, default=0,
                                              verbose_name='Unit Tests Coverage')
    defects_in_dev = models.PositiveIntegerField(default=0, verbose_name='Defects in Dev')
    elicitation_analysis_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                                    verbose_name='Research Time')  # in hours
    customer_facing_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                               validators=[MinValueValidator(Decimal(0))],
                                               verbose_name='Customer Facing Time')  # in hours
    documentation_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                             validators=[MinValueValidator(Decimal(0))],
                                             verbose_name='Documentation Time')  # in hours
    ticketless_dev_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                              validators=[MinValueValidator(Decimal(0))],
                                              verbose_name='Ticketless Development Time')  # in hours

    # Quality
    uat_defects_not_prevented = models.PositiveIntegerField(default=0, verbose_name='Externally Reported Defects')

    # Usage
    pheme_manual_tests = models.PositiveIntegerField(default=0, verbose_name='Pheme Manual Tests')
    pheme_auto_tests = models.PositiveIntegerField(default=0, verbose_name='Pheme Auto Tests')
    visilog_txl_parsed = models.PositiveIntegerField(default=0, verbose_name='Visilog TXL Parsed')
    visilog_txl_schema_violation = models.PositiveIntegerField(default=0, verbose_name='Visilog Schema Violatoin')
    ceeq_daily_summaries = models.PositiveIntegerField(default=0, verbose_name='CEEQ Daily Summaries')

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

    @property
    def external_savings(self):
        return self.visilog_txl_parsed * 0.33 + self.pheme_manual_tests * 1.79 + self.pheme_auto_tests * 1.97

    @property
    def internal_savings(self):
        return self.ceeq_daily_summaries * 20 + self.other_savings

    @classmethod
    def quality_graph(cls):
        data = cls.objects.filter(subteam=None).order_by("-created")[:12]
        return {'title': 'Externally Reported Defects',
                'data': [{'date': week.created.strftime("%b %-d"), 'value': week.uat_defects_not_prevented} for week in data]}

    @classmethod
    def efficiency_graph(cls):
        data = cls.objects.filter(subteam=None).order_by("-created")[:12]
        return {'title': 'Story Point Backlog',
                'data': [{'date': week.created.strftime("%b %-d"), 'value': week.story_points_backlog} for week in data]}

    @classmethod
    def throughput_graph(cls):
        data = cls.objects.filter(subteam=None).order_by("-created")[:12]
        return {'title': 'Savings',
                'data': [{'date': week.created.strftime("%b %-d"),
                          'value': week.pheme_auto_tests * 1.97 + week.pheme_manual_tests * 1.79 + float(week.other_savings)}
                         for week in data]}

    @classmethod
    def progress_graph(cls):
        data = cls.objects.filter(subteam=None).order_by("-created")[:4]
        # print [week.unit_tests_coverage for week in data]
        return {'title': 'Unit Test Coverage',
                'data': {'positive': {'value': sum([week.unit_tests_coverage for week in data]), 'label': 'Covered'},
                         'negative': {'value': sum([1-week.unit_tests_coverage for week in data]), 'label': 'Uncovered'}}}

    class Meta:
        verbose_name_plural = "Innovation Metrics"


class RequirementMetrics(BaseMetrics):
    """
    Metrics for group: Requirements Engineering
    """

    # Throughput
    backlog = models.PositiveIntegerField(default=0, verbose_name='Backlog')
    team_initiative = models.PositiveIntegerField(default=0, verbose_name='Team Initiative')
    time_initiatives = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                            verbose_name='Initiatives Time')
    elicitation_analysis_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                                    verbose_name='Research Time')  # in hours
    # Project Work
    active_projects = models.PositiveIntegerField(default=0, verbose_name='Project WIP')
    srs_initial = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='SRS Initial Time')
    srs_detail = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='SRS Detail Time')
    gap_analysis = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='GAP Analysis Time')
    project_time = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Project Time')

    # Levels of Efforts
    project_loe = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Project LOE'S")
    project_actuals = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Project Actual's")

    # Quality
    revisions = models.PositiveIntegerField(default=0, verbose_name='Rework')
    creep = models.PositiveIntegerField( default=0, verbose_name='Scope Creep')
    rework_external_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                                verbose_name='Scope Creep Time')

    # SLAs
    # This is now system_miss as it's pulling from Personal now
    slas_missed = models.DecimalField(max_digits=3, decimal_places=2, default=0,
                                      verbose_name='SLAs Missed')
    system_met = models.PositiveIntegerField(default=0, verbose_name='System SLA Met')
    system_miss = models.PositiveIntegerField(default=0, verbose_name='System SLA Miss')
    actual_met = models.PositiveIntegerField(default=0, verbose_name='Actual SLA Met')
    actual_miss = models.PositiveIntegerField(default=0, verbose_name='Actual SLA Miss')
    # system_met = models.DecimalField(max_digits=3, decimal_places=2, default=0, verbose_name='System SLA Met')
    # system_miss = models.DecimalField(max_digits=3, decimal_places=2, default=0, verbose_name='System SLA Miss')
    # actual_met = models.DecimalField(max_digits=3, decimal_places=2, default=0, verbose_name='Actual SLA Met')
    # actual_miss = models.DecimalField(max_digits=3, decimal_places=2, default=0, verbose_name='Actual SLA Miss')

    # Optimization
    optimization_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                             verbose_name="Optimization Time")
    # Costs
    travel_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                      verbose_name='Travel Costs')

    survey = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Survey')

    @property
    def staff_minus_manager(self):
        return self.staffs - 1

    @property
    def avg_throughput(self):
        return self.active_projects + self.team_initiative

    @property
    # this is now deprecated and has been replaced with utilization
    def gross_available_time(self):
        return self.staffs * 6 * 5

    @property
    def utilization(self):
        util_avg = (self.project_time + self.time_initiatives)/((self.staffs - 1 + self.contractors)* 8 * 5)
        return '{0:.2f}%'.format(util_avg * 100)

    @property
    def utilization_time(self):
        return self.project_time + self.time_initiatives

    @property
    def efficiency(self):
        eff_avg = (self.srs_initial + self.srs_detail + self.gap_analysis +
                   self.time_initiatives + self.creep + self.rework_external_time) /\
                  ((self.staff_minus_manager + self.contractors)* 6 * 5)
        return '{0:.2f}%'.format(eff_avg * 100)

    @property
    def efficiency_time(self):
        return self.srs_initial + self.srs_detail + self.gap_analysis + self.time_initiatives

    @property
    def rework_external_cost(self):
        return self.rework_external_time * 50

    @property
    def operational_cost(self):
        return (self.staffs - 1 + self.contractors) * 30 * 50

    @property
    def total_operational_cost(self):
        return self.operational_cost + self.license_cost

    @property
    def overall_cost(self):
        return self.total_operational_cost + self.travel_cost

    @classmethod
    def quality_graph(cls):
        data = cls.objects.filter(subteam=None).order_by("-created")[:12]
        return {'title': 'Revisions',
                'data': [{'date': week.created.strftime("%b %-d"), 'value': week.revisions} for week in data]}

    @classmethod
    def efficiency_graph(cls):
        data = cls.objects.filter(subteam=None).order_by("-created")[:12]
        return {'title': 'Utilization',
                'data': [{'date': week.created.strftime("%b %-d"), 'value': week.gross_available_time} for week in data],
                'thresholds': {'too_high': 1,
                               'upper_ideal': .85,
                               'lower_ideal': .7}}

    @classmethod
    def throughput_graph(cls):
        data = cls.objects.filter(subteam=None).order_by("-created")[:12]
        return {'title': 'Backlog',
                'data': [{'date': week.created.strftime("%b %-d"), 'value': week.backlog} for week in data]}

    @classmethod
    def progress_graph(cls):
        data = cls.objects.filter(subteam=None).order_by("-created")[:12]
        return {'title': 'Requirement Standardization',
                'data': {'positive': {'value': 0, 'label': 'Automatic'},
                         'negative': {'value': 1, 'label': 'Manual'}}}

    class Meta:
        verbose_name_plural = "Requirement Metrics"


class LabMetrics(BaseMetrics):
    """
    Metrics for group: Test Lab
    """
    # Throughput
    tickets_received = models.PositiveIntegerField(default=0, verbose_name='Tickets Received')
    tickets_closed = models.PositiveIntegerField(default=0, verbose_name='Tickets Closed')
    virtual_machines = models.PositiveIntegerField(default=0, verbose_name='Virtual Machines')
    physical_machines = models.PositiveIntegerField(default=0, verbose_name='Physical Machines')
    monitor_machines = models.PositiveIntegerField(default=0,
                                                   verbose_name='Machines under Monitoring')
    administration_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                              validators=[MinValueValidator(Decimal(0))],
                                              verbose_name='Administration Time')  # in hours
    project_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                       validators=[MinValueValidator(Decimal(0))],
                                       verbose_name='Project Time')  # in hours
    ticket_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                      validators=[MinValueValidator(Decimal(0))],
                                      verbose_name='Ticket Time')  # in hours

    # Quality
    builds_submitted = models.PositiveIntegerField(default=0, verbose_name='Builds Submitted')
    builds_accepted = models.PositiveIntegerField(default=0, verbose_name='Builds Accepted')
    platform_drift_violations = models.PositiveIntegerField(default=0,
                                                            verbose_name='Platform Drift Violations')
    updates_install_docs = models.PositiveIntegerField(default=0,
                                                       verbose_name='Updates to Install Docs')

    # Costs
    power_consumption_ups_a = models.PositiveIntegerField(default=0,
                                                          verbose_name='Power Consumption UPS A')  # in kw
    power_consumption_ups_b = models.PositiveIntegerField(default=0,
                                                          verbose_name='Power Consumption UPS B')  # in kw

    @property
    def utilization(self):
        if (self.staffs * 40 - self.pto_holiday_time) != 0:
            return (self.administration_time + self.project_time + self.ticket_time) / (self.staffs * 40 - self.pto_holiday_time)
        else:
            return 0

    @property
    def efficiency(self):
        if self.staffs != 0:
            return (self.administration_time + self.project_time + self.ticket_time) / (self.staffs * 30)
        else:
            return 0

    @property
    def builds_rejected(self):
        return self.builds_submitted - self.builds_accepted

    @classmethod
    def quality_graph(cls):
        data = cls.objects.filter(subteam=None).order_by("-created")[:12]
        return {'title': 'Power Consumption',
                'data': [{'date': week.created.strftime("%b %-d"), 'value': week.power_consumption_ups_a + week.power_consumption_ups_b} for week in data]}

    @classmethod
    def efficiency_graph(cls):
        data = cls.objects.filter(subteam=None).order_by("-created")[:12]
        return {'title': 'Ticket Handling',
                'data': [{'date': week.created.strftime("%b %-d"),
                          'value': week.tickets_closed - week.tickets_received} for week in data],
                'allow_negative': True,
                'thresholds': {'too_high': 500,
                               'upper_ideal': 250,
                               'lower_ideal': 0}}

    @classmethod
    def throughput_graph(cls):
        data = cls.objects.filter(subteam=None).order_by("-created")[:12]
        return {'title': 'Lab Machines',
                'data': [{'date': week.created.strftime("%b %-d"), 'value': week.virtual_machines + week.physical_machines} for week in data]}

    @classmethod
    def progress_graph(cls):
        data = cls.objects.filter(subteam=None).order_by("-created")[:6]
        return {'title': 'A vs B',
                'data': {'positive': {'value': sum([week.power_consumption_ups_a for week in data]), 'label': 'A'},
                         'negative': {'value': sum([week.power_consumption_ups_b for week in data]), 'label': 'B'}}}

    class Meta:
        verbose_name_plural = "Lab Metrics"


class TestMetricsConfiguration(models.Model):
    """
    Configuration of Test Metric costs
    """
    functional_group = models.ForeignKey('users.FunctionalGroup')
    hours_per_week = models.PositiveSmallIntegerField(default=0)
    costs_per_hour_staff = models.PositiveSmallIntegerField(default=0)
    costs_per_hour_contractor = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return '{0}: {1}: {2}: {3}'.format(self.functional_group.key,
                                           self.hours_per_week,
                                           self.costs_per_hour_staff,
                                           self.costs_per_hour_contractor)
