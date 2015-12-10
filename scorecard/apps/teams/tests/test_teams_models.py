from datetime import datetime
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
        self.staffs = 2
        self.contractors = 1
        self.story_points_execution = 32
        self.license_cost = 135.65

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


