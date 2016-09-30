from django.db import models

from scorecard.apps.users.models import FunctionalGroup, HumanResource, Subteam
from utils import calculate_business_day, REVENUE_SCALE_CHOICES, SMALL_REVENUE


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')
    revenue_scale = models.IntegerField(choices=REVENUE_SCALE_CHOICES, default=SMALL_REVENUE)

    def __unicode__(self):
        return self.name


class ProjectPhase(models.Model):
    project = models.ForeignKey(Project)
    subteam = models.ForeignKey(Subteam)

    lead = models.ForeignKey(HumanResource, related_name='phase_lead')  # lead on ProjectPhase
    worker = models.ManyToManyField(HumanResource, related_name='phase_worker', blank=True)  # humanResources on ProjectPhase

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
                                      self.subteam)

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
    subteam = models.ForeignKey(Subteam)

    lead = models.ForeignKey(HumanResource, related_name='ticket_lead')
    worker = models.ManyToManyField(HumanResource, related_name='ticket_worker', blank=True)
    revenue_scale = models.IntegerField(choices=REVENUE_SCALE_CHOICES, default=SMALL_REVENUE)

    key = models.CharField(max_length=50)

    estimate_start = models.DateTimeField(null=True, blank=True)
    estimate_end = models.DateTimeField(null=True, blank=True)
    actual_start = models.DateTimeField(null=True, blank=True)
    actual_end = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return '{0}: {1}: {2}'.format(self.key,
                                      self.lead.user,
                                      self.subteam)

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


