from django.contrib.auth.models import User
from django.db import models


class FunctionalGroup(models.Model):
    """
    Functional Group, such as RE, QA, QI, PQ, TL
    """
    name = models.CharField(max_length=50, unique=True, default='')

    def __unicode__(self):
        return self.name


class HumanResource(models.Model):
    """
    Link to auth user
    """
    functional_group = models.ForeignKey(FunctionalGroup, null=True, blank=True)
    user = models.OneToOneField(User)

    manager = models.BooleanField(default=False)
    contractor = models.BooleanField(default=False)

    def __unicode__(self):
        return '{0}: {1}'.format(self.user.username, self.functional_group.name)
