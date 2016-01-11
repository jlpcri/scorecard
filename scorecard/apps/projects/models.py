from django.utils import timezone
from django.db import models

from scorecard.apps.users.models import FunctionalGroup, HumanResource


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')

    def __unicode__(self):
        return self.name


class ProjectPhase(models.Model):
    project = models.ForeignKey(Project)
    functional_group = models.ForeignKey(FunctionalGroup)
    lead = models.ForeignKey(HumanResource)

    name = models.CharField(max_length=50, default='')
    key = models.CharField(max_length=50, default='')

    estimate_start = models.DateTimeField()
    estimate_end = models.DateTimeField()
    actual_start = models.DateTimeField()
    actual_end = models.DateTimeField()

    class Meta:
        unique_together = ('project', 'name')

    def __unicode__(self):
        return '{0}: {1}: {2}'.format(self.name,
                                      self.project.name,
                                      self.functional_group.key)

    def save(self, *args, **kwargs):
        self.estimate_start = timezone.now()
        self.estimate_end = timezone.now()
        self.actual_start = timezone.now()
        self.actual_end = timezone.now()

        return super(ProjectPhase, self).save(*args, **kwargs)


class Ticket(models.Model):
    functional_group = models.ForeignKey(FunctionalGroup)
    lead = models.ForeignKey(HumanResource)

    key = models.CharField(max_length=50, default='')

    estimate_start = models.DateTimeField()
    estimate_end = models.DateTimeField()
    actual_start = models.DateTimeField()
    actual_end = models.DateTimeField()

    def __unicode__(self):
        return '{0}: {1}: {2}'.format(self.key,
                                      self.lead.user,
                                      self.functional_group.key)

    def save(self, *args, **kwargs):
        self.estimate_start = timezone.now()
        self.estimate_end = timezone.now()
        self.actual_start = timezone.now()
        self.actual_end = timezone.now()

        return super(Ticket, self).save(*args, **kwargs)
