from django.db import models
from django.utils.timezone import localtime
import time

from scorecard.apps.users.models import FunctionalGroup


def script_location(instance, filename):
    return '{0}_{1}'.format(str(time.time()).replace('.', ''), filename)


class Automation(models.Model):
    """
    Let user upload python script to automatically fetch data from Server: JIRA, ISR, Confluence, Pheme etc.
    """
    functional_group = models.ForeignKey('users.FunctionalGroup')
    tests_run = models.PositiveIntegerField(default=0)  # how many times to click Tested button
    last_success = models.DateTimeField(auto_now=True, db_index=True)
    last_failure = models.DateTimeField(auto_now=True, db_index=True)
    last_successful_run = models.BooleanField(default=True)
    result = models.DecimalField(max_digits=15, decimal_places=2, default=0)  # result of script running

    script_name = models.TextField(default='')
    script_file = models.FileField(upload_to=script_location, blank=True, null=True)

    column_field = models.CharField(max_length=50)

    class Meta:
        unique_together = (("functional_group", "column_field"), )

    def __unicode__(self):
        return '{0}: {1}: {2}: {3}'.format(self.functional_group.abbreviation,
                                           self.column_field,
                                           self.tests_run,
                                           localtime(self.last_success))




