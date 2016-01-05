from django.db import models
from django.utils.timezone import localtime

from scorecard.apps.users.models import FunctionalGroup, HumanResource


class InnovationStats(models.Model):
    """
    Personal Performance status for QI team
    """
    human_resource = models.ForeignKey(HumanResource)
    analysis_hours = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    story_points_worked = models.PositiveIntegerField(default=0)


class TestLabStats(models.Model):
    """
    Personal Performance status for TL team
    """
    human_resource = models.ForeignKey(HumanResource)
    tickets_closed = models.PositiveIntegerField(default=0)


class RequirementStats(models.Model):
    """
    Personal Performance status for RE team
    """
    human_resource = models.ForeignKey(HumanResource)


class TestStats(models.Model):
    """
    Personal Performance status for PQ, QA, TE team
    """
    human_resource = models.ForeignKey(HumanResource)

    tc_manual_dev = models.PositiveIntegerField(default=0)
    tc_manual_execution = models.PositiveIntegerField(default=0)
    tc_auto_dev = models.PositiveIntegerField(default=0)
    tc_auto_execution = models.PositiveIntegerField(default=0)

    tickets_worked = models.PositiveIntegerField(default=0)
    initiatives_worked_hours = models.DecimalField(max_digits=10, decimal_places=2, default=0)




