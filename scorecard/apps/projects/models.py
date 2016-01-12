from django.utils import timezone
from django.db import models

from scorecard.apps.users.models import FunctionalGroup, HumanResource


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True, default='')

    def __unicode__(self):
        return self.name

    @property
    def phases_pq(self):
        return self.projectphase_set.filter(functional_group__key='PQ')

    @property
    def phases_qa(self):
        return self.projectphase_set.filter(functional_group__key='QA')

    @property
    def phases_te(self):
        return self.projectphase_set.filter(functional_group__key='TE')

    @property
    def phases_qi(self):
        return self.projectphase_set.filter(functional_group__key='QI')

    @property
    def phases_re(self):
        return self.projectphase_set.filter(functional_group__key='RE')

    @property
    def phases_tl(self):
        return self.projectphase_set.filter(functional_group__key='TL')


class ProjectPhase(models.Model):
    project = models.ForeignKey(Project)
    functional_group = models.ForeignKey(FunctionalGroup)
    lead = models.ForeignKey(HumanResource)

    name = models.CharField(max_length=50, default='')
    key = models.CharField(max_length=50, default='')

    estimate_start = models.DateTimeField(null=True, blank=True)
    estimate_end = models.DateTimeField(null=True, blank=True)
    actual_start = models.DateTimeField(null=True, blank=True)
    actual_end = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('project', 'name')

    def __unicode__(self):
        return '{0}: {1}: {2}'.format(self.name,
                                      self.project.name,
                                      self.functional_group.key)


class Ticket(models.Model):
    functional_group = models.ForeignKey(FunctionalGroup)
    lead = models.ForeignKey(HumanResource)

    key = models.CharField(max_length=50, default='')

    estimate_start = models.DateTimeField(null=True, blank=True)
    estimate_end = models.DateTimeField(null=True, blank=True)
    actual_start = models.DateTimeField(null=True, blank=True)
    actual_end = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return '{0}: {1}: {2}'.format(self.key,
                                      self.lead.user,
                                      self.functional_group.key)


