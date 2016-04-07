from django.utils import timezone
from django.db import models

from scorecard.apps.users.models import FunctionalGroup, HumanResource, Subteam
from utils import calculate_business_day


class Project(models.Model):
    # Revenue Scale Options
    LARGE_REVENUE = 1
    MEDIUM_REVENUE = 2
    SMALL_REVENUE = 3
    REVENUE_SCALE_CHOICES = (
        (LARGE_REVENUE, 'Greater than 1M'),
        (MEDIUM_REVENUE, 'Between 250K and 1M'),
        (SMALL_REVENUE, 'Less than 250K')
    )

    name = models.CharField(max_length=50, unique=True, default='')
    revenue_scale = models.IntegerField(choices=REVENUE_SCALE_CHOICES, default=SMALL_REVENUE)

    def __unicode__(self):
        return self.name


class ProjectPhase(models.Model):
    project = models.ForeignKey(Project)
    functional_group = models.ForeignKey(FunctionalGroup)
    subteam = models.ForeignKey(Subteam, blank=True, null=True)

    lead = models.ForeignKey(HumanResource, related_name='phase_lead')  # lead on ProjectPhase
    worker = models.ManyToManyField(HumanResource, related_name='phase_worker')  # humanResources on ProjectPhase

    name = models.CharField(max_length=50)
    key = models.CharField(max_length=50, null=True, blank=True)

    estimate_start = models.DateTimeField(null=True, blank=True)
    estimate_end = models.DateTimeField(null=True, blank=True)
    actual_start = models.DateTimeField(null=True, blank=True)
    actual_end = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('project', 'name')

    def __unicode__(self):
        return '{0}: {1}: {2}'.format(self.project.name,
                                      self.name,
                                      self.functional_group.abbreviation)

    @property
    def start_delays(self):
        if self.estimate_start and self.actual_start:
            data = calculate_business_day(self.estimate_start, self.actual_start)
        else:
            data = 'Null'

        return data

    @property
    def diff_durations(self):
        if self.estimate_start and self.estimate_end and self.actual_start and self.actual_end:
            data = calculate_business_day(self.actual_start, self.actual_end)\
                   - calculate_business_day(self.estimate_start, self.estimate_end)
        else:
            data = 'Null'

        return data


class Ticket(models.Model):
    functional_group = models.ForeignKey(FunctionalGroup)
    subteam = models.ForeignKey(Subteam, blank=True, null=True)

    lead = models.ForeignKey(HumanResource, related_name='ticket_lead')
    worker = models.ManyToManyField(HumanResource, related_name='ticket_worker')
    revenue_scale = models.IntegerField(choices=Project.REVENUE_SCALE_CHOICES, default=Project.SMALL_REVENUE)

    key = models.CharField(max_length=50)

    estimate_start = models.DateTimeField(null=True, blank=True)
    estimate_end = models.DateTimeField(null=True, blank=True)
    actual_start = models.DateTimeField(null=True, blank=True)
    actual_end = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return '{0}: {1}: {2}'.format(self.key,
                                      self.lead.user,
                                      self.functional_group.abbreviation)


