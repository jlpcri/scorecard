from datetime import datetime
import random
from django.test import TestCase
from django.utils.timezone import localtime
import pytz

from scorecard.apps.teams.models import InnovationMetrics, LabMetrics, RequirementMetrics, TestMetrics, FunctionalGroup, TestMetricsConfiguration


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
            name='Requirement Engineering',
            key='RE'
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


class LabMetricsModelTest(TestCase):
    def setUp(self):
        self.functional_group = FunctionalGroup.objects.create(
            name='Test Lab',
            key='TL'
        )
        self.lab = LabMetrics.objects.create(
            functional_group=self.functional_group,
            created=datetime.utcnow().replace(tzinfo=pytz.utc),
            confirmed=datetime.utcnow().replace(tzinfo=pytz.utc)
        )

    def test_string_representations(self):
        self.assertEqual(str(self.lab), '{0}: {1}: {2}'.format(self.lab.functional_group.name,
                                                               localtime(self.lab.confirmed),
                                                               localtime(self.lab.created)))

    def test_verbose_name_plural(self):
        self.assertEqual(str(LabMetrics._meta.verbose_name_plural), 'lab metricss')


class TestMetricsModelTest(TestCase):
    def setUp(self):
        self.functional_group = FunctionalGroup.objects.create(
            name='Quality Assurance',
            key='QA'
        )
        self.functional_group_pq = FunctionalGroup.objects.create(
            name='Product Quality',
            key='PQ'
        )
        self.functional_group_te = FunctionalGroup.objects.create(
            name='Test Engineering',
            key='TE'
        )
        self.functional_group_others = FunctionalGroup.objects.create(
            name='Other Group',
            key='OG'
        )
        self.test_metric_config_pq = TestMetricsConfiguration.objects.create(
            functional_group=self.functional_group_pq,
            hours_per_week=random.randint(1, 100),
            costs_per_hour_staff=random.randint(1, 100),
            costs_per_hour_contractor=random.randint(1, 100)
        )
        self.test_metric_config_qa = TestMetricsConfiguration.objects.create(
            functional_group=self.functional_group,
            hours_per_week=random.randint(1, 100),
            costs_per_hour_staff=random.randint(1, 100),
            costs_per_hour_contractor=random.randint(1, 100)
        )
        self.test_metric_config_te = TestMetricsConfiguration.objects.create(
            functional_group=self.functional_group_te,
            hours_per_week=random.randint(1, 100),
            costs_per_hour_staff=random.randint(1, 100),
            costs_per_hour_contractor=random.randint(1, 100)
        )
        self.test_metric = TestMetrics.objects.create(
            functional_group=self.functional_group,
            created=datetime.utcnow().replace(tzinfo=pytz.utc),
            confirmed=datetime.utcnow().replace(tzinfo=pytz.utc)
        )
        self.staffs = random.randint(1, 100)
        self.contractors = random.randint(1, 100)

        self.tc_manual_dev = random.random() * 100
        self.tc_auto_dev = random.random() * 100

        self.tc_manual_execution = random.random() * 100
        self.tc_auto_execution = random.random() * 100

        self.tc_manual_dev_time = random.random() * 100
        self.tc_auto_dev_time = random.random() * 100

        self.tc_manual_execution_time = random.random() * 100
        self.tc_auto_execution_time = random.random() * 100

        self.project_prep = random.randint(1, 100)
        self.project_execution = random.randint(1, 100)

        self.ticket_prep = random.randint(1, 100)
        self.ticket_execution = random.randint(1, 100)

        self.license_cost = random.random() * 100

    def test_string_representations(self):
        self.assertEqual(str(self.test_metric), '{0}: {1}: {2}'.format(self.test_metric.functional_group.name,
                                                                       localtime(self.test_metric.confirmed),
                                                                       localtime(self.test_metric.created)))

    def test_verbose_name_plural(self):
        self.assertEqual(str(TestMetrics._meta.verbose_name_plural), 'test metricss')

    def test_auto_footprint_dev_age_none_of_both(self):
        self.assertEqual(self.test_metric.auto_footprint_dev_age, 0)

    def test_auto_footprint_dev_age_only_tc_manual_dev(self):
        self.test_metric.tc_maual_dev = self.tc_manual_dev
        self.test_metric.save()

        self.assertEqual(self.test_metric.auto_footprint_dev_age, 0)

    def test_auto_footprint_dev_age_only_tc_auto_dev(self):
        self.test_metric.tc_auto_dev = self.tc_auto_dev
        self.test_metric.save()

        self.assertEqual(self.test_metric.auto_footprint_dev_age, 1)

    def test_auto_footprint_dev_age(self):
        self.test_metric.tc_manual_dev = self.tc_manual_dev
        self.test_metric.tc_auto_dev = self.tc_auto_dev
        self.test_metric.save()

        self.assertEqual(self.test_metric.auto_footprint_dev_age,
                         self.tc_auto_dev / (self.tc_manual_dev + self.tc_auto_dev))

    def test_auto_footprint_execution_age_none_of_both(self):
        self.assertEqual(self.test_metric.auto_footprint_execution_age, 0)

    def test_auto_footprint_execution_age_only_tc_manual_execution(self):
        self.test_metric.tc_manual_execution = self.tc_manual_execution
        self.test_metric.save()

        self.assertEqual(self.test_metric.auto_footprint_execution_age, 0)

    def test_auto_footprint_execution_age_only_tc_auto_execution(self):
        self.test_metric.tc_auto_execution = self.tc_auto_execution
        self.test_metric.save()

        self.assertEqual(self.test_metric.auto_footprint_execution_age, 1)

    def test_auto_footprint_execution_age(self):
        self.test_metric.tc_manual_execution = self.tc_manual_execution
        self.test_metric.tc_auto_execution = self.tc_auto_execution
        self.test_metric.save()

        self.assertEqual(self.test_metric.auto_footprint_execution_age,
                         self.tc_auto_execution / (self.tc_manual_execution + self.tc_auto_execution))

    def test_avg_throughput_no_human_resources(self):
        self.assertEqual(self.test_metric.avg_throughput, 0)

    def test_avg_throughput(self):
        self.test_metric.staffs = self.staffs
        self.test_metric.contractors = self.contractors
        self.test_metric.tc_manual_dev = self.tc_manual_dev
        self.test_metric.tc_manual_execution = self.tc_manual_execution
        self.test_metric.tc_auto_dev = self.tc_auto_dev
        self.test_metric.tc_auto_execution = self.tc_auto_execution
        self.test_metric.save()

        self.assertEqual(round(self.test_metric.avg_throughput, 10),
                         round((self.tc_manual_dev + self.tc_auto_dev + self.tc_manual_execution + self.tc_auto_execution) / (self.staffs + self.contractors), 10))

    def test_active_projects(self):
        self.test_metric.project_prep = self.project_prep
        self.test_metric.project_execution = self.project_execution
        self.test_metric.save()

        self.assertEqual(self.test_metric.active_projects,
                         self.project_prep + self.project_execution)

    def test_active_tickets(self):
        self.test_metric.ticket_prep = self.ticket_prep
        self.test_metric.ticket_execution = self.ticket_execution
        self.test_metric.save()

        self.assertEqual(self.test_metric.active_tickets,
                         self.ticket_prep + self.ticket_execution)

    def test_auto_and_execution_time(self):
        self.test_metric.tc_manual_dev_time = self.tc_manual_dev_time
        self.test_metric.tc_auto_dev_time = self.tc_auto_dev_time
        self.test_metric.tc_manual_execution_time = self.tc_manual_execution_time
        self.test_metric.tc_auto_execution_time = self.tc_auto_execution_time
        self.test_metric.save()

        self.assertEqual(round(self.test_metric.auto_and_execution_time, 6),
                         round(self.tc_manual_dev_time + self.tc_auto_dev_time + self.tc_manual_execution_time + self.tc_auto_execution_time, 6))

    def test_gross_available_time(self):
        self.test_metric.staffs = self.staffs
        self.test_metric.contractors = self.contractors
        self.test_metric.save()

        self.assertEqual(self.test_metric.gross_available_time,
                         (self.staffs + self.contractors) * 30)

    def test_efficiency_no_human_resources(self):
        self.assertEqual(self.test_metric.efficiency, 0)

    def test_efficiency(self):
        self.test_metric.staffs = self.staffs
        self.test_metric.contractors = self.contractors
        self.test_metric.tc_manual_dev_time = self.tc_manual_dev_time
        self.test_metric.tc_auto_dev_time = self.tc_auto_dev_time
        self.test_metric.tc_manual_execution_time = self.tc_manual_execution_time
        self.test_metric.tc_auto_execution_time = self.tc_auto_execution_time
        self.test_metric.save()

        auto_execution_time = self.tc_manual_dev_time + self.tc_auto_dev_time + self.tc_manual_execution_time + self.tc_auto_execution_time
        gross_available = (self.staffs + self.contractors) * 30

        self.assertEqual(round(self.test_metric.efficiency, 10),
                         round(auto_execution_time / gross_available, 10))

    def test_operational_cost_qa(self):
        self.test_metric.staffs = self.staffs
        self.test_metric.contractors = self.contractors
        self.test_metric.save()

        test_configs = self.functional_group.testmetricsconfiguration_set.all()
        if len(test_configs) > 0:
            hours = test_configs[0].hours_per_week
            rate_staff = test_configs[0].costs_per_hour_staff
            rate_contractor = test_configs[0].costs_per_hour_contractor
        else:
            hours, rate_staff, rate_contractor = 0, 0, 0

        self.assertEqual(self.test_metric.operational_cost,
                         self.staffs * hours * rate_staff + self.contractors * hours * rate_contractor)

    def test_operational_cost_pq(self):
        self.test_metric.functional_group = self.functional_group_pq
        self.test_metric.staffs = self.staffs
        self.test_metric.contractors = self.contractors
        self.test_metric.save()

        test_configs = self.functional_group_pq.testmetricsconfiguration_set.all()
        if len(test_configs) > 0:
            hours = test_configs[0].hours_per_week
            rate_staff = test_configs[0].costs_per_hour_staff
            rate_contractor = test_configs[0].costs_per_hour_contractor
        else:
            hours, rate_staff, rate_contractor = 0, 0, 0

        self.assertEqual(self.test_metric.operational_cost,
                         self.staffs * hours * rate_staff + self.contractors * hours * rate_contractor)

    def test_operational_cost_te(self):
        self.test_metric.functional_group = self.functional_group_te
        self.test_metric.staffs = self.staffs
        self.test_metric.contractors = self.contractors
        self.test_metric.save()

        test_configs = self.functional_group_te.testmetricsconfiguration_set.all()
        if len(test_configs) > 0:
            hours = test_configs[0].hours_per_week
            rate_staff = test_configs[0].costs_per_hour_staff
            rate_contractor = test_configs[0].costs_per_hour_contractor
        else:
            hours, rate_staff, rate_contractor = 0, 0, 0

        self.assertEqual(self.test_metric.operational_cost,
                         self.staffs * hours * rate_staff + self.contractors * hours * rate_contractor)

    def test_total_operational_cost_qa(self):
        self.test_metric.staffs = self.staffs
        self.test_metric.contractors = self.contractors
        self.test_metric.license_cost = self.license_cost
        self.test_metric.save()

        self.assertEqual(self.test_metric.total_operational_cost,
                         self.test_metric.operational_cost + self.license_cost)

    def test_total_operational_cost_pq(self):
        self.test_metric.functional_group = self.functional_group_pq
        self.test_metric.staffs = self.staffs
        self.test_metric.contractors = self.contractors
        self.test_metric.license_cost = self.license_cost
        self.test_metric.save()

        self.assertEqual(self.test_metric.total_operational_cost,
                         self.test_metric.operational_cost + self.license_cost)

    def test_total_operational_cost_te(self):
        self.test_metric.functional_group = self.functional_group_te
        self.test_metric.staffs = self.staffs
        self.test_metric.contractors = self.contractors
        self.test_metric.license_cost = self.license_cost
        self.test_metric.save()

        self.assertEqual(self.test_metric.total_operational_cost,
                         self.test_metric.operational_cost + self.license_cost)

    def test_auto_savings_qa(self):
        self.test_metric.tc_auto_execution_time = self.tc_auto_execution_time
        self.test_metric.save()

        test_configs = self.functional_group.testmetricsconfiguration_set.all()
        if len(test_configs) > 0:
            rate = test_configs[0].costs_per_hour_staff
        else:
            rate = 0

        self.assertEqual(self.test_metric.auto_savings,
                         self.tc_auto_execution_time * rate)

    def test_auto_savings_pq(self):
        self.test_metric.functional_group = self.functional_group_pq
        self.test_metric.tc_auto_execution_time = self.tc_auto_execution_time
        self.test_metric.save()

        test_configs = self.functional_group_pq.testmetricsconfiguration_set.all()
        if len(test_configs) > 0:
            rate = test_configs[0].costs_per_hour_staff
        else:
            rate = 0

        self.assertEqual(self.test_metric.auto_savings,
                         self.tc_auto_execution_time * rate)

    def test_auto_savings_te(self):
        self.test_metric.functional_group = self.functional_group_te
        self.test_metric.tc_auto_execution_time = self.tc_auto_execution_time
        self.test_metric.save()

        test_configs = self.functional_group_te.testmetricsconfiguration_set.all()
        if len(test_configs) > 0:
            rate = test_configs[0].costs_per_hour_staff
        else:
            rate = 0

        self.assertEqual(self.test_metric.auto_savings,
                         self.tc_auto_execution_time * rate)

    def test_auto_savings_others(self):
        self.test_metric.functional_group = self.functional_group_others
        self.test_metric.tc_auto_execution_time = self.tc_auto_execution_time
        self.test_metric.save()

        self.assertEqual(self.test_metric.auto_savings, 0)


class TestMetricsConfigurationModelTest(TestCase):
    def setUp(self):
        self.functional_group = FunctionalGroup.objects.create(
            name='Quality Innovation',
            key='QI'
        )
        self.test_config = TestMetricsConfiguration.objects.create(
            functional_group=self.functional_group,
            hours_per_week=random.randint(1, 100),
            costs_per_hour_staff=random.randint(1, 100),
            costs_per_hour_contractor=random.randint(1, 100)
        )

    def test_string_representations(self):
        self.assertEqual(str(self.test_config), '{0}: {1}: {2}: {3}'.format(self.test_config.functional_group.key,
                                                                            self.test_config.hours_per_week,
                                                                            self.test_config.costs_per_hour_staff,
                                                                            self.test_config.costs_per_hour_contractor))

    def test_verbose_name_plural(self):
        self.assertEqual(str(TestMetricsConfiguration._meta.verbose_name_plural), 'test metrics configurations')
