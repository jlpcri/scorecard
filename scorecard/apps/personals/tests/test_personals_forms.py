import random
from django.contrib.auth.models import User
from django.test import TestCase

from scorecard.apps.personals.models import InnovationStats, LabStats, RequirementStats, TestStats
from scorecard.apps.personals.forms import InnovationForm, LabForm, RequirementForm, TestForm
from scorecard.apps.users.models import FunctionalGroup, HumanResource


class InnovationFormTest(TestCase):
    def setUp(self):
        self.fg_qi = FunctionalGroup.objects.create(
            name='Quality Innovation',
            key='QI'
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
        self.personal_stat = InnovationStats.objects.create(
            human_resource=self.hr
        )

    def test_innovation_form_valid_with_valid_params(self):
        data = {
            'overtime_weekday': random.randint(1, 100),
            'overtime_weekend': random.randint(1, 100),
            'rework_time': random.randint(1, 100),
            'story_points_execution': random.randint(1, 100),
            'unit_tests_dev': random.randint(1, 100),
            'elicitation_analysis_time': random.randint(1, 100)
        }
        form = InnovationForm(instance=self.personal_stat, data=data)
        self.assertTrue(form.is_valid())

    def test_innovation_form_invalid_with_blank(self):
        form = InnovationForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'overtime_weekday': ['This field is required.'],
            'overtime_weekend': ['This field is required.'],
            'rework_time': ['This field is required.'],
            'story_points_execution': ['This field is required.'],
            'unit_tests_dev': ['This field is required.'],
            'elicitation_analysis_time': ['This field is required.']
        })


class LabFormTest(TestCase):
    def setUp(self):
        self.fg_tl = FunctionalGroup.objects.create(
            name='Test Lab',
            key='TL'
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
        self.personal_stat = LabStats.objects.create(
            human_resource=self.hr
        )

    def test_lab_form_valid_with_valid_params(self):
        data = {
            'overtime_weekday': random.randint(1, 100),
            'overtime_weekend': random.randint(1, 100),
            'rework_time': random.randint(1, 100),
            'tickets_closed': random.randint(1, 100)
        }
        form = LabForm(instance=self.personal_stat, data=data)
        self.assertTrue(form.is_valid())

    def test_lab_form_invalid_with_blank(self):
        form = LabForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'overtime_weekday': ['This field is required.'],
            'overtime_weekend': ['This field is required.'],
            'rework_time': ['This field is required.'],
            'tickets_closed': ['This field is required.']
        })


class RequirementFormTest(TestCase):
    def setUp(self):
        self.fg_re = FunctionalGroup.objects.create(
            name='Requirment Engineering',
            key='RE'
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
        self.personal_stat = RequirementStats.objects.create(
            human_resource=self.hr
        )

    def test_requirement_form_valid_with_valid_params(self):
        data = {
            'overtime_weekday': random.randint(1, 100),
            'overtime_weekend': random.randint(1, 100),
            'rework_time': random.randint(1, 100),
            'elicitation_analysis_time': random.randint(1, 100),
            'revisions': random.randint(1, 100),
            'rework_external_time': random.randint(1, 100),
            'travel_cost': random.randint(1, 100)
        }
        form = RequirementForm(instance=self.personal_stat, data=data)
        self.assertTrue(form.is_valid())

    def test_requirement_form_invalid_with_blank(self):
        form = RequirementForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'overtime_weekday': ['This field is required.'],
            'overtime_weekend': ['This field is required.'],
            'rework_time': ['This field is required.'],
            'elicitation_analysis_time': ['This field is required.'],
            'revisions': ['This field is required.'],
            'rework_external_time': ['This field is required.'],
            'travel_cost': ['This field is required.']
        })


class TestFormTest(TestCase):
    def setUp(self):
        self.fg_qa = FunctionalGroup.objects.create(
            name='Quality Assurance',
            key='QA'
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
        self.personal_stat = LabStats.objects.create(
            human_resource=self.hr
        )

    def test_test_form_valid_with_valid_params(self):
        data = {
            'overtime_weekday': random.randint(1, 100),
            'overtime_weekend': random.randint(1, 100),
            'rework_time': random.randint(1, 100),
            'tc_manual_dev': random.randint(1, 100),
            'tc_manual_dev_time': random.randint(1, 100),
            'tc_manual_execution': random.randint(1, 100),
            'tc_manual_execution_time': random.randint(1, 100),
            'tc_auto_dev': random.randint(1, 100),
            'tc_auto_dev_time': random.randint(1, 100),
            'tc_auto_execution': random.randint(1, 100),
            'tc_auto_execution_time': random.randint(1, 100),
            'defect_caught': random.randint(1, 100),
            'uat_defects_not_prevented': random.randint(1, 100),
            'standards_violated': random.randint(1, 100),
            'resource_swap_time': random.randint(1, 100)
        }
        form = TestForm(instance=self.personal_stat, data=data)
        self.assertTrue(form.is_valid())

    def test_test_form_invalid_with_blank(self):
        form = TestForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'overtime_weekday': ['This field is required.'],
            'overtime_weekend': ['This field is required.'],
            'rework_time': ['This field is required.'],
            'tc_manual_dev': ['This field is required.'],
            'tc_manual_dev_time': ['This field is required.'],
            'tc_manual_execution': ['This field is required.'],
            'tc_manual_execution_time': ['This field is required.'],
            'tc_auto_dev': ['This field is required.'],
            'tc_auto_dev_time': ['This field is required.'],
            'tc_auto_execution': ['This field is required.'],
            'tc_auto_execution_time': ['This field is required.'],
            'defect_caught': ['This field is required.'],
            'uat_defects_not_prevented': ['This field is required.'],
            'standards_violated': ['This field is required.'],
            'resource_swap_time': ['This field is required.']
        })
