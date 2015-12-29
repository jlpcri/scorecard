from django.db import models

from scorecard.apps.users.models import FunctionalGroup, HumanResource


class Projects(models.Model):
    """
    Project lists for each team
    """
    name = models.CharField(max_length=50, default='')
    functional_group = models.ForeignKey(FunctionalGroup)

    class Meta:
        unique_together = ('name', 'functional_group', )

    def __unicode__(self):
        return '{0}: {1}'.format(self.name, self.functional_group.key)


class DefiningObjectives(models.Model):
    name = models.CharField(max_length=50, default='')


class BaseIndividual(models.Model):
    """
    Base Individual for all teams
    """
    human_resource = models.ForeignKey(HumanResource)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    confirmed = models.DateTimeField(auto_now=True, db_index=True)
    updated = models.BooleanField(default=False)

    compliments = models.PositiveIntegerField(default=0)
    complaints = models.PositiveIntegerField(default=0)
    escalations = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class ProductQualityIndividual(BaseIndividual):
    pass


class QualityAssuranceIndividual(BaseIndividual):
    pass


class TestEngineeringIndividual(BaseIndividual):
    pass


class QualityInnovationIndividual(BaseIndividual):
    pass


class RequirementsEngineeringIndividual(BaseIndividual):
    pass


class TestLabIndividual(BaseIndividual):
    pass


class BaseTestInitiativesIndividual(models.Model):
    """
    Base Entry for Test Metric (PQ, QA, TE) Individual - Initiatives
    """

    time_savings = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cost_savings = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    systemic_methods = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        abstract = True


class BaseTestProjectsIndividual(models.Model):
    """
    Base Entry for Test Metric (PQ, QA, TE) Individual - Projects
    """

    test_plan_days_late = models.PositiveIntegerField(default=0)

    tc_days_late = models.PositiveIntegerField(default=0)
    tc_manual = models.PositiveIntegerField(default=0)
    tc_auto = models.PositiveIntegerField(default=0)

    requirement_days_late = models.PositiveIntegerField(default=0)

    tc_exec_days_late = models.PositiveIntegerField(default=0)
    tc_exec_manual = models.PositiveIntegerField(default=0)
    tc_exec_auto = models.PositiveIntegerField(default=0)

    sla_escalations = models.PositiveIntegerField(default=0)
    sla_swaps = models.PositiveIntegerField(default=0)
    sla_weekend = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sla_overtime_hours = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    uat_ceeq = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    uat_defects = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sdis = models.PositiveIntegerField(default=0)
    standards_violations = models.PositiveIntegerField(default=0)
    rework_introduced_hours = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        abstract = True


class PQInitiatives(BaseTestInitiativesIndividual):
    pq_individual = models.ForeignKey(ProductQualityIndividual)
    defining_objective = models.ForeignKey(DefiningObjectives)


class PQProjects(BaseTestProjectsIndividual):
    pq_individual = models.ForeignKey(ProductQualityIndividual)
    project = models.ForeignKey(Projects)


class QAInitiatives(BaseTestInitiativesIndividual):
    qa_individual = models.ForeignKey(QualityAssuranceIndividual)
    defining_objective = models.ForeignKey(DefiningObjectives)


class QAProjects(BaseTestProjectsIndividual):
    qa_individual = models.ForeignKey(QualityAssuranceIndividual)
    project = models.ForeignKey(Projects)

    quality_engineering_days_late = models.PositiveIntegerField(default=0)
    test_data_request_days_late = models.PositiveIntegerField(default=0)


class TEInitiatives(BaseTestInitiativesIndividual):
    te_individual = models.ForeignKey(TestEngineeringIndividual)
    defining_objective = models.ForeignKey(DefiningObjectives)


class TEProjects(BaseTestProjectsIndividual):
    te_individual = models.ForeignKey(TestEngineeringIndividual)
    project = models.ForeignKey(Projects)