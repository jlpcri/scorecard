from django.db import models
from django.utils.timezone import localtime
import time

from scorecard.apps.users.models import FunctionalGroup


def script_location(instance, filename):
    return '{0}_{1}'.format(str(time.time()).replace('.', ''), filename)


class BaseAutomation(models.Model):
    """
    Let user upload python script to automatically fetch data from Server: JIRA, ISR, Confluence, Pheme etc.
    """
    COMPLIMENTS = 'compliments'
    COMPLAINTS = 'complaints'
    ESCALATIONS = 'escalations'

    functional_group = models.ForeignKey(FunctionalGroup)
    tests_run = models.PositiveIntegerField(default=0)  # how many times to click Tested button
    last_success = models.DateTimeField(auto_now=True, db_index=True)
    last_failure = models.DateTimeField(auto_now=True, db_index=True)
    last_successful_run = models.BooleanField(default=True)
    result = models.DecimalField(max_digits=15, decimal_places=2, default=0)  # result of script running

    script_name = models.TextField()
    script_file = models.FileField(upload_to=script_location)

    COLUMN_FIELDS_CHOICES = (
        (COMPLIMENTS, 'Compliments'),
        (COMPLAINTS, 'Complaints'),
        (ESCALATIONS, 'Escalations'),
    )

    class Meta:
        abstract = True


class InnovationAutomation(BaseAutomation):
    """
    Automation for groups: QI
    """

    BACKLOG_STORY = 'story_points_backlog'
    STORY_POINTS_PREP = 'story_points_prep'
    UNIT_TESTS_COVER = 'unit_tests_coverage'
    DOCUMENT_COVER = 'documentation_coverage'
    DEFECTS_IN_DEV = 'defects_in_dev'
    REVISIONS = 'revisions'
    ACTIVE_PROJECTS = 'active_projects'

    SLAS_MET = 'slas_met'
    DELAYS_INTRODUCED_TIME = 'delays_introduced_time'
    SDIS_NOT_PREVENTED = 'sdis_not_prevented'
    UAT_DEFECTS_NOT_PREVENTED = 'uat_defects_not_prevented'
    RESOURCE_SWAP = 'resource_swap'
    ESCALATIONS = 'escalations'
    REWORK_INTRODUCED_TIME = 'rework_introduced_time'

    AVERAGE_TEAM_SIZE = 'avg_team_size'
    RESOURCE_SWAP_TIME = 'resource_swap_time'

    LICENSE_COST = 'license_cost'
    OTHER_SAVINGS = 'other_savings'

    PHEME_MANUAL_TESTS = 'pheme_manual_tests'
    PHEME_AUTO_TESTS = 'pheme_auto_tests'
    VISILOG_TXL_PARSED = 'visilog_txl_parsed'
    VISILOG_TXL_VIOLATION = 'visilog_txl_schema_violation'

    COLUMN_FIELDS_CHOICES = BaseAutomation.COLUMN_FIELDS_CHOICES + (
        (BACKLOG_STORY, 'Story Points Backlog'),
        (STORY_POINTS_PREP, 'Story Points Prep'),
        (UNIT_TESTS_COVER, 'Unit Tests Coverage'),
        (DOCUMENT_COVER, 'Documentation Coverage'),
        (DEFECTS_IN_DEV, 'Defects In Dev'),
        (REVISIONS, 'Revisions'),
        (ACTIVE_PROJECTS, 'Active Projects'),

        (SLAS_MET, 'SLAs Met'),
        (DELAYS_INTRODUCED_TIME, 'Delays Introduced Time'),
        (SDIS_NOT_PREVENTED, 'SDIs Not Prevented'),
        (UAT_DEFECTS_NOT_PREVENTED, 'Uat Defects Not Prevented'),
        (RESOURCE_SWAP, 'Resource Swap'),
        # (ESCALATIONS, 'Escalations'),
        (REWORK_INTRODUCED_TIME, 'Rework Introduced Time'),

        (AVERAGE_TEAM_SIZE, 'Average Team Size'),
        (RESOURCE_SWAP_TIME, 'Resource Swap Time'),

        (LICENSE_COST, 'License Cost'),
        (OTHER_SAVINGS, 'Other Savings'),

        (PHEME_MANUAL_TESTS, 'Pheme Manual Tests'),
        (PHEME_AUTO_TESTS, 'Pheme Auto Tests'),
        (VISILOG_TXL_PARSED, 'Visilog TXL Parsed'),
        (VISILOG_TXL_VIOLATION, 'Visilog TXL Schema Violation')
    )

    column_field = models.CharField(max_length=50,
                                    choices=COLUMN_FIELDS_CHOICES,
                                    default=BaseAutomation.COMPLIMENTS,
                                    unique=True)

    def __unicode__(self):
        return '{0}: {1}: {2}: {3}'.format(self.functional_group.key,
                                           self.column_field,
                                           self.tests_run,
                                           localtime(self.last_success))


class LabAutomation(BaseAutomation):
    """
    Automation for groups: TL
    """
    TICKETS_RECEIVED = 'tickets_received'
    # TICKETS_CLOSED = 'tickets_closed'
    VIRTUAL_MACHINES = 'virtual_machines'
    PHYSICAL_MACHINES = 'physical_machines'
    POWER_UPS_A = 'power_consumption_ups_a'
    POWER_UPS_B = 'power_consumption_upb_b'
    LICENSE_COST = 'license_cost'

    COLUMN_FIELDS_CHOICES = BaseAutomation.COLUMN_FIELDS_CHOICES + (
        (TICKETS_RECEIVED, 'Tickets Received'),
        (VIRTUAL_MACHINES, 'Virtual Machines'),
        (PHYSICAL_MACHINES, 'Physical Machines'),
        (POWER_UPS_A, 'Power Consumption UPS A'),
        (POWER_UPS_B, 'Power Consumption UPS B'),
        (LICENSE_COST, 'License Cost')
    )
    column_field = models.CharField(max_length=50,
                                    choices=COLUMN_FIELDS_CHOICES,
                                    default=BaseAutomation.COMPLIMENTS,
                                    unique=True)

    def __unicode__(self):
        return '{0}: {1}: {2}: {3}'.format(self.functional_group.key,
                                           self.column_field,
                                           self.tests_run,
                                           localtime(self.last_success))


class RequirementAutomation(BaseAutomation):
    """
    Automation for groups: RE
    """
    BACKLOG = 'backlog'
    ACTIVE_PROJECTS = 'active_projects'
    TEAM_INITIATIVE = 'team_initiative'
    # ELICITATION_ANALYSIS_TIME = ''
    # REVISIONS = ''
    REWORK_INTRO_TIME = 'rework_introduced_time'
    SLAS_MET = 'slas_met'
    SLAS_MISSED = 'slas_missed'
    DELAYS_INTRO_TIME = 'delays_introduced_time'
    # TRAVEL_COST = 'travel_cost'

    COLUMN_FIELDS_CHOICES = BaseAutomation.COLUMN_FIELDS_CHOICES + (
        (BACKLOG, 'Backlog'),
        (ACTIVE_PROJECTS, 'Active Projects'),
        (TEAM_INITIATIVE, 'Team Initiative'),
        (REWORK_INTRO_TIME, 'Rework Introduced Time'),
        (SLAS_MET, 'SLAs Met'),
        (SLAS_MISSED, 'SLAs Missed'),
        (DELAYS_INTRO_TIME, 'Delays Introduced Time'),
    )

    column_field = models.CharField(max_length=50,
                                    choices=COLUMN_FIELDS_CHOICES,
                                    default=BaseAutomation.COMPLIMENTS,
                                    unique=True)

    def __unicode__(self):
        return '{0}: {1}: {2}: {3}'.format(self.functional_group.key,
                                           self.column_field,
                                           self.tests_run,
                                           localtime(self.last_success))


class TestAutomation(BaseAutomation):
    """
    Automation for groups: QA, TE
    """
    TEAM_INITIATIVE = 'team_initiative'
    TICKET_BACKLOG = 'ticket_backlog'
    TICKET_PREP = 'ticket_prep'
    TICKET_EXECUTION = 'ticket_execution'
    TICKET_CLOSED = 'ticket_closed'
    PROJECT_BACKLOG = 'project_backlog'
    PROJECT_PREP = 'project_prep'
    PROJECT_EXECUTION = 'project_execution'
    PROJECT_CLOSED = 'project_closed'

    SLAS_MET = 'slas_met'
    DELAYS_INTRO_TIME = 'delays_introduced_time'
    SDIS_NOT_PREVENTED = 'sdis_not_prevented'
    RESOURCE_SWAP = 'resource_swap'
    REWORK_INTRO_TIME = 'rework_introduced_time'

    AVERAGE_TEAM_SIZE = 'avg_team_size'
    AVERAGE_TIME_FRAME = 'avg_time_frame'

    LICENSE_COST = 'license_cost'
    OTHER_SAVINGS = 'other_savings'

    COLUMN_FIELDS_CHOICES = BaseAutomation.COLUMN_FIELDS_CHOICES + (
        (TEAM_INITIATIVE, 'Team Initiative'),
        (TICKET_BACKLOG, 'Ticket Backlog'),
        (TICKET_PREP, 'Ticket Prep'),
        (TICKET_EXECUTION, 'Ticket Execution'),
        (TICKET_CLOSED, 'Ticket Closed'),
        (PROJECT_BACKLOG, 'Project Backlog'),
        (PROJECT_PREP, 'Project Prep'),
        (PROJECT_EXECUTION, 'Project Execution'),
        (PROJECT_CLOSED, 'Project Closed'),
        (SLAS_MET, 'SLAs Met'),
        (DELAYS_INTRO_TIME, 'Delays Introduced Time'),
        (SDIS_NOT_PREVENTED, 'SDIs Not Prevented'),
        (RESOURCE_SWAP, 'Resource Swap'),
        (REWORK_INTRO_TIME, 'Rework Introduced Time'),
        (AVERAGE_TEAM_SIZE, 'Average Team Size'),
        (AVERAGE_TIME_FRAME, 'Average Time Frame'),
        (LICENSE_COST, 'License Cost'),
        (OTHER_SAVINGS, 'Other Savings')
    )

    column_field = models.CharField(max_length=50,
                                    choices=COLUMN_FIELDS_CHOICES,
                                    default=BaseAutomation.COMPLIMENTS)

    class Meta:
        unique_together = ('functional_group', 'column_field')

    def __unicode__(self):
        return '{0}: {1}: {2}: {3}'.format(self.functional_group.key,
                                           self.column_field,
                                           self.tests_run,
                                           localtime(self.last_success))
