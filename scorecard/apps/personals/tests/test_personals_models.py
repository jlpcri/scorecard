from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from django.utils.timezone import localtime

from scorecard.apps.personals.models import (InnovationStats, LabStats,
                                             RequirementStats, TestStats)
from scorecard.apps.users.models import FunctionalGroup, HumanResource


class InnovationStatsModelTest(TestCase):
    def setUp(self):
        self.fg_qi = FunctionalGroup.objects.create(
            name='Quality Innovation',
            abbreviation='QI'
        )
        self.user_account = {
            'username': 'UserName',
            'password': 'PassWord'
        }
        self.user = User.objects.create_user(
            username=self.user_account['username'],
            password=self.user_account['password']
        )
        self.hr = HumanResource.objects.create(
            functional_group=self.fg_qi,
            user=self.user,
            manager=True
        )
        self.personal = InnovationStats.objects.create(
            human_resource=self.hr,
            created=timezone.now()
        )

    def test_string_representations(self):
        self.assertEqual(str(self.personal), '{0}: {1}: {2}'.format(self.personal.human_resource.user.username,
                                                                    self.personal.human_resource.functional_group.key,
                                                                    localtime(self.personal.created)))

    def test_verbose_name_plural(self):
        self.assertEqual(str(InnovationStats._meta.verbose_name_plural), 'innovation statss')


class LabStatsModelTest(TestCase):
    def setUp(self):
        self.fg_tl = FunctionalGroup.objects.create(
            name='Test Lab',
            abbreviation='TL'
        )
        self.user_account = {
            'username': 'UserName',
            'password': 'PassWord'
        }
        self.user = User.objects.create_user(
            username=self.user_account['username'],
            password=self.user_account['password']
        )
        self.hr = HumanResource.objects.create(
            functional_group=self.fg_tl,
            user=self.user,
            manager=True
        )
        self.personal = LabStats.objects.create(
            human_resource=self.hr,
            created=timezone.now()
        )

    def test_string_representations(self):
        self.assertEqual(str(self.personal), '{0}: {1}: {2}'.format(self.personal.human_resource.user.username,
                                                                    self.personal.human_resource.functional_group.key,
                                                                    localtime(self.personal.created)))

    def test_verbose_name_plural(self):
        self.assertEqual(str(LabStats._meta.verbose_name_plural), 'lab statss')


class RequirementStatsModelTest(TestCase):
    def setUp(self):
        self.fg_re = FunctionalGroup.objects.create(
            name='Requirment Engineering',
            abbreviation='RE'
        )
        self.user_account = {
            'username': 'UserName',
            'password': 'PassWord'
        }
        self.user = User.objects.create_user(
            username=self.user_account['username'],
            password=self.user_account['password']
        )
        self.hr = HumanResource.objects.create(
            functional_group=self.fg_re,
            user=self.user,
            manager=True
        )
        self.personal = RequirementStats.objects.create(
            human_resource=self.hr,
            created=timezone.now()
        )

    def test_string_representations(self):
        self.assertEqual(str(self.personal), '{0}: {1}: {2}'.format(self.personal.human_resource.user.username,
                                                                    self.personal.human_resource.functional_group.key,
                                                                    localtime(self.personal.created)))

    def test_verbose_name_plural(self):
        self.assertEqual(str(RequirementStats._meta.verbose_name_plural), 'requirement statss')


class TestStatsModelTest(TestCase):
    def setUp(self):
        self.fg_qa = FunctionalGroup.objects.create(
            name='Quality Assurance',
            abbreviation='QA'
        )
        self.user_account = {
            'username': 'UserName',
            'password': 'PassWord'
        }
        self.user = User.objects.create_user(
            username=self.user_account['username'],
            password=self.user_account['password']
        )
        self.hr = HumanResource.objects.create(
            functional_group=self.fg_qa,
            user=self.user,
            manager=True
        )
        self.personal = TestStats.objects.create(
            human_resource=self.hr,
            created=timezone.now()
        )

    def test_string_representations(self):
        self.assertEqual(str(self.personal), '{0}: {1}: {2}'.format(self.personal.human_resource.user.username,
                                                                    self.personal.human_resource.functional_group.key,
                                                                    localtime(self.personal.created)))

    def test_verbose_name_plural(self):
        self.assertEqual(str(TestStats._meta.verbose_name_plural), 'test statss')
