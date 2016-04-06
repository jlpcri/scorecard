from operator import itemgetter
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.timezone import localtime

from scorecard.apps.users.models import FunctionalGroup, HumanResource


class BaseStats(models.Model):
    """
    Base Individual Status for all teams
    """
    human_resource = models.ForeignKey(HumanResource)
    created = models.DateTimeField(db_index=True)
    confirmed = models.DateTimeField(auto_now=True, db_index=True)
    updated = models.BooleanField(default=False)

    # Efficiency
    overtime_weekday = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                           verbose_name='Overtime Weekday')  # in hours
    overtime_weekend = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                           verbose_name='Overtime Weekend')  # in hours
    rework_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                      verbose_name='Rework Time')  # in hours
    pto_holiday_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                           verbose_name='PTO/Holiday Time')  # in hours

    class Meta:
        abstract = True
        ordering = ['-created']

    def __unicode__(self):
        return '{0}: {1}: {2}'.format(self.human_resource.user.username,
                                      self.human_resource.functional_group.key,
                                      localtime(self.created))

    def stat_summary(self):
        return {'Overtime': self.overtime_weekday+self.overtime_weekend, 'Rework': self.rework_time}


class InnovationStats(BaseStats):
    """
    Personal Performance status for QI team
    """
    # Throughput
    story_points_execution = models.PositiveIntegerField(default=0, verbose_name='Story Points Execution')
    unit_tests_dev = models.PositiveIntegerField(default=0, verbose_name='Unit Tests Dev')
    elicitation_analysis_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                                    verbose_name='Research Time')  # in hours
    customer_facing_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                               validators=[MinValueValidator(Decimal(0))],
                                               verbose_name='Customer Facing Time')
    documentation_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                             validators=[MinValueValidator(Decimal(0))],
                                             verbose_name='Documentation Time')
    ticketless_dev_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                              validators=[MinValueValidator(Decimal(0))],
                                              verbose_name='Ticketless Development Time')

    def stat_summary(self):
        return {'Story Points': self.story_points_execution, 'Unit Tests': self.unit_tests_dev}


class LabStats(BaseStats):
    """
    Personal Performance status for TL team
    """
    # Throughput
    tickets_closed = models.PositiveIntegerField(default=0, verbose_name='Ticket Closed')
    administration_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                              validators=[MinValueValidator(Decimal(0))],
                                              verbose_name='Administration hours')
    project_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                       validators=[MinValueValidator(Decimal(0))],
                                       verbose_name='Project hours')
    ticket_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                      validators=[MinValueValidator(Decimal(0))],
                                      verbose_name='Ticket hours')

    # Quality
    builds_submitted = models.PositiveIntegerField(default=0, verbose_name='Builds Submitted')
    builds_accepted = models.PositiveIntegerField(default=0, verbose_name='Builds Accepted')
    updates_install_docs = models.PositiveIntegerField(default=0,
                                                       verbose_name='Updates to install documents')

    def stat_summary(self):
        return {'Overtime': self.overtime_weekday+self.overtime_weekend, 'Tickets Closed': self.tickets_closed}


class RequirementStats(BaseStats):
    """
    Personal Performance status for RE team
    """
    # Throughput
    elicitation_analysis_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                                    verbose_name='Research Time')  # in hours

    # Quality
    revisions = models.PositiveIntegerField(default=0, verbose_name='Revisions')

    # Efficiency
    rework_external_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                               verbose_name='Rework External Time')

    # Costs
    travel_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                      verbose_name='Travel Costs')

    def stat_summary(self):
        return {'Analysis/Elicitation': self.elicitation_analysis_time, 'Overtime': self.overtime_weekday+self.overtime_weekend, 'Rework': self.rework_time}


class TestStats(BaseStats):
    """
    Personal Performance status for QA, TE team
    """
    # Throughput
    tc_manual_dev = models.PositiveIntegerField(default=0,
                                                verbose_name='TC Manual Dev')
    tc_manual_dev_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                             verbose_name='TC Manual Dev Time')  # in hours
    tc_manual_execution = models.PositiveIntegerField(default=0,
                                                      verbose_name='TC Manual Exec')
    tc_manual_execution_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                                   verbose_name='TC Manual Exec Time')  # in hours
    tc_auto_dev = models.PositiveIntegerField(default=0,
                                              verbose_name='TC Auto Dev')
    tc_auto_dev_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                           verbose_name='TC Auto Dev Time')  # in hours
    tc_auto_execution = models.PositiveIntegerField(default=0,
                                                    verbose_name='TC Auto Exec')
    tc_auto_execution_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                                 verbose_name='TC Auto Exec Time')  # in hours
    estimate_auto_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                             validators=[MinValueValidator(Decimal(0))],
                                             verbose_name='Estimated Manual Time for Automation')
    standard_work_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                             validators=[MinValueValidator(Decimal(0))],
                                             verbose_name='Standard Work Time')  #  hours spent doing test documentation and associated overhead

    # Quality
    defect_caught = models.PositiveIntegerField(default=0,
                                                verbose_name='Defects Caught')
    uat_defects_not_prevented = models.PositiveIntegerField(default=0,
                                                            verbose_name='UAT Defects not Prevented')
    standards_violated = models.PositiveIntegerField(default=0,
                                                     verbose_name='Standards Violated')

    # Efficiency
    resource_swap_time = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                             verbose_name='Resource Swap Time')  # in hours
    loe_deviation = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                        verbose_name='LOE deviation Time')  #  in hours

    def stat_summary(self):
        return {'Manual Tests Developed': self.tc_manual_dev,
                'Manual Tests Executed': self.tc_manual_execution,
                'Automatic Tests Developed': self.tc_auto_dev,
                'Automatic Tests Executed': self.tc_auto_execution}

    @property
    def phase_delay_and_duration(self):
        data = []
        phases = self.human_resource.projectphase_set.all()
        for phase in phases:
            temp = {}
            temp['project'] = phase.project.name
            temp['phase'] = phase.name
            temp['start_delay'] = phase.start_delays
            temp['diff_duration'] = phase.diff_durations

            data.append(temp)

        data.sort(key=itemgetter('project'))
        data.sort(key=itemgetter('phase'))

        return data

    @property
    def phases_lead_count(self):
        phases = self.human_resource.projectphase_set.all()

        return len(phases)

    @property
    def tickets_worked(self):
        tickets = self.human_resource.ticket_set.all()

        return len(tickets)

