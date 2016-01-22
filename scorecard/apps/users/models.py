from django.contrib.auth.models import User
from django.db import models


class FunctionalGroup(models.Model):
    """
    Functional Group, such as RE, QA, QI, TL
    """
    KEY_CHOICES = (
        ('QA', 'Quality Assurance'),
        ('QI', 'Quality Innovation'),
        ('RE', 'Requirement Engineering'),
        ('TE', 'Test Engineering'),
        ('TL', 'Test Lab')
    )

    name = models.CharField(max_length=50, unique=True, default='')
    key = models.CharField(max_length=10, choices=KEY_CHOICES, default='')

    def __unicode__(self):
        return '{0}: {1}'.format(self.name, self.key)


    class Meta:
        verbose_name_plural = "Functional Groups"


class HumanResource(models.Model):
    """
    Link to auth user
    """
    functional_group = models.ForeignKey(FunctionalGroup, null=True, blank=True)
    user = models.OneToOneField(User)

    manager = models.BooleanField(default=False)
    contractor = models.BooleanField(default=False)

    def __unicode__(self):
        if self.functional_group:
            return '{0}: {1}: {2}'.format(self.user.username,
                                          self.functional_group.key,
                                          self.manager)
        else:
            return '{0}: {1}: {2}'.format(self.user.username, 'No Team',  self.manager)


class ColumnPreference(models.Model):
    user = models.ForeignKey(User)

    # this is name of the table that will have rows that can be shown or hidden
    table_name = models.CharField(default='change me', max_length=50, blank=False)

    # this is a comma delimited list of columns the user wants to hide
    hide_list = models.CharField(default='', max_length=50, blank=True)

    def __unicode__(self):
        return str(self.user.username) + "  " + self.table_name + "  " + str(self.hide_list)

    class Meta:
        ordering = ('user',)
        verbose_name = "Column Preference"

