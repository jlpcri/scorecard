import time

from django.db import models
from django.utils.timezone import localtime

from scorecard.apps.users.models import FunctionalGroup


def script_location(instance, filename):
    if instance.human_resource:
        location = '{0}_{1}_{2}'.format(str(time.time()).replace('.', ''),
                                        instance.human_resource.user.username,
                                        filename)
    else:
        location = '{0}_{1}'.format(str(time.time()).replace('.', ''),
                                    filename)
    return location


class Automation(models.Model):
    """
    Let user upload python script to automatically fetch data from Server: JIRA, ISR, Confluence, Pheme etc.
    """
    # functional_group = models.ForeignKey('users.FunctionalGroup')
    subteam = models.ForeignKey('users.Subteam', blank=True, null=True)
    human_resource = models.ForeignKey('users.HumanResource', blank=True, null=True)

    tests_run = models.PositiveIntegerField(default=0)  # how many times to click Tested button
    last_success = models.DateTimeField(auto_now=True, db_index=True)
    last_failure = models.DateTimeField(auto_now=True, db_index=True)
    last_successful_run = models.BooleanField(default=True)
    result = models.DecimalField(max_digits=15, decimal_places=2, default=0)  # result of script running

    script_name = models.TextField(default='')
    script_file = models.FileField(upload_to=script_location, blank=True, null=True)

    column_field = models.CharField(max_length=50)

    class Meta:
        unique_together = (("subteam", "column_field"), ("human_resource", "column_field"), )

    def __unicode__(self):
        if self.subteam:
            return '{0}: {1}: {2}: {3}'.format(self.subteam.parent.abbreviation,
                                               self.column_field,
                                               self.tests_run,
                                               localtime(self.last_success))
        else:
            return '{0}: {1}: {2}: {3}'.format(self.human_resource,
                                               self.column_field,
                                               self.tests_run,
                                               localtime(self.last_success))
