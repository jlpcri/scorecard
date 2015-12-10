from datetime import datetime
import random
from django.test import TestCase
from django.utils.timezone import localtime
import pytz

from scorecard.apps.teams.models import InnovationMetrics, LabMetrics, RequirementMetrics, TestMetrics, FunctionalGroup


class InnovationMetricsModelTest(TestCase):
    def setUp(self):
        self.functional_group = FunctionalGroup.objects.create(
            name='Quality Innovation',
            key='QI'
        )
        self.innovation = InnovationMetrics(
            functional_group=self.functional_group,
            created=datetime.utcnow().replace(tzinfo=pytz.utc),
            confirmed=datetime.utcnow().replace(tzinfo=pytz.utc)
        )
        self.staffs = random.randint(1, 100)
        self.contractors = random.randint(1, 100)
        self.story_points_execution = random.random() * 100
        self.license_cost = random.random() * 100

    def test_string_representations(self):
        self.assertEqual(str(self.innovation), '{0}: {1}: {2}'.format(self.innovation.functional_group.name,
                                                                      localtime(self.innovation.confirmed),
                                                                      localtime(self.innovation.created)))

    def test_verbose_name_plural(self):
        self.assertEqual(str(InnovationMetrics._meta.verbose_name_plural), 'innovation metricss')

    def test_avg_throughput_no_staffs(self):
        self.assertEqual(self.innovation.avg_throughput, 0)

    def test_avg_throughput(self):
        self.innovation.staffs = self.staffs
        self.innovation.story_points_execution = self.story_points_execution
        self.innovation.save()

        self.assertEqual(self.innovation.avg_throughput, self.story_points_execution / self.staffs)

    def test_operational_cost(self):
        self.innovation.staffs = self.staffs
        self.innovation.contractors = self.contractors
        self.innovation.save()

        self.assertEqual(self.innovation.operational_cost, (self.staffs + self.contractors) * 40 * 45)

    def test_total_operational_cost(self):
        self.innovation.staffs = self.staffs
        self.innovation.contractors = self.contractors
        self.innovation.license_cost = self.license_cost
        self.innovation.save()

        self.assertEqual(self.innovation.total_operational_cost,
                         self.innovation.operational_cost + self.license_cost
                         )


class RequirementMetricsModelTest(TestCase):
    def setUp(self):
        self.functional_group = FunctionalGroup.objects.create(
            name='Quality Innovation',
            key='QI'
        )
        self.requirement = RequirementMetrics.objects.create(
            functional_group=self.functional_group,
            created=datetime.utcnow().replace(tzinfo=pytz.utc),
            confirmed=datetime.utcnow().replace(tzinfo=pytz.utc)
        )
        self.staffs = random.randint(1, 100)
        self.contractors = random.randint(1, 100)
        self.active_projects = random.randint(1, 100)
        self.team_initiative = random.randint(1, 100)
        self.elicitation_analysis_time = random.random() * 100
        self.rework_external_time = random.random() * 100
        self.license_cost = random.random() * 100
        self.travel_cost = random.random() * 100

    def test_string_representations(self):
        self.assertEqual(str(self.requirement), '{0}: {1}: {2}'.format(self.requirement.functional_group.name,
                                                                       localtime(self.requirement.confirmed),
                                                                       localtime(self.requirement.created)))

    def test_verbose_name_plural(self):
        self.assertEqual(str(RequirementMetrics._meta.verbose_name_plural), 'requirement metricss')

    def test_avg_throughput(self):
        self.requirement.active_projects = self.active_projects
        self.requirement.team_initiative = self.team_initiative
        self.requirement.save()

        self.assertEqual(self.requirement.avg_throughput,
                         self.active_projects + self.team_initiative)

    def test_gross_available_time(self):
        self.requirement.staffs = self.staffs
        self.requirement.save()

        self.assertEqual(self.requirement.gross_available_time, self.staffs * 6 * 5)

    def test_efficiency_no_staffs(self):
        self.assertEqual(self.requirement.efficiency, 0)

    def test_efficiency(self):
        self.requirement.staffs = self.staffs
        self.requirement.elicitation_analysis_time = self.elicitation_analysis_time
        self.requirement.save()

        self.assertEqual(self.requirement.efficiency, self.elicitation_analysis_time / self.requirement.gross_available_time)

    def test_rework_external_cost(self):
        self.requirement.rework_external_time = self.rework_external_time
        self.requirement.save()

        self.assertEqual(self.requirement.rework_external_cost,
                         self.rework_external_time * 50)

    def test_operational_cost(self):
        self.requirement.staffs = self.staffs
        self.requirement.contractors = self.contractors
        self.requirement.save()

        self.assertEqual(self.requirement.operational_cost,
                         (self.staffs + self.contractors) * 30 * 50)

    def test_total_operational_cost(self):
        self.requirement.staffs = self.staffs
        self.requirement.contractors = self.contractors
        self.requirement.license_cost = self.license_cost
        self.requirement.save()

        self.assertEqual(self.requirement.total_operational_cost,
                         self.requirement.operational_cost + self.license_cost)

    def test_overall_cost(self):
        self.requirement.staffs = self.staffs
        self.requirement.contractors = self.contractors
        self.requirement.license_cost = self.license_cost
        self.requirement.travel_cost = self.travel_cost
        self.requirement.save()

        self.assertEqual(self.requirement.overall_cost,
                         self.requirement.total_operational_cost + self.travel_cost)

