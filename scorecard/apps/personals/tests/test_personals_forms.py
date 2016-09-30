import random
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from scorecard.apps.personals.models import InnovationStats, LabStats, RequirementStats, TestStats
from scorecard.apps.personals.forms import InnovationForm, LabForm, RequirementForm, TestForm
from scorecard.apps.users.models import FunctionalGroup, HumanResource


class InnovationFormTest(TestCase):
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
        self.personal_stat = InnovationStats.objects.create(
            human_resource=self.hr,
            created=timezone.now()
        )

    def test_innovation_form_valid_with_valid_params(self):
        data = {}
        for field in InnovationForm().fields:
            data[field] = random.randint(1, 100)
        form = InnovationForm(instance=self.personal_stat, data=data)
        self.assertTrue(form.is_valid())

    def test_innovation_form_invalid_with_blank(self):
        form = InnovationForm({})
        self.assertFalse(form.is_valid())
        errors = {}
        for field in InnovationForm().fields:
            errors[field] = ['This field is required.']
        self.assertEqual(form.errors, errors)


class LabFormTest(TestCase):
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
        self.personal_stat = LabStats.objects.create(
            human_resource=self.hr,
            created=timezone.now()
        )

    def test_lab_form_valid_with_valid_params(self):
        data = {}
        for field in LabForm().fields:
            data[field] = random.randint(1, 100)

        form = LabForm(instance=self.personal_stat, data=data)
        self.assertTrue(form.is_valid())

    def test_lab_form_invalid_with_blank(self):
        form = LabForm({})
        self.assertFalse(form.is_valid())
        errors = {}
        for field in LabForm().fields:
            errors[field] = ['This field is required.']
        self.assertEqual(form.errors, errors)


class RequirementFormTest(TestCase):
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
        self.personal_stat = RequirementStats.objects.create(
            human_resource=self.hr,
            created=timezone.now()
        )

    def test_requirement_form_valid_with_valid_params(self):
        data = {}
        for field in RequirementForm().fields:
            data[field] = random.randint(1, 100)
        form = RequirementForm(instance=self.personal_stat, data=data)
        self.assertTrue(form.is_valid())

    def test_requirement_form_invalid_with_blank(self):
        form = RequirementForm({})
        self.assertFalse(form.is_valid())
        errors = {}
        for field in RequirementForm().fields:
            errors[field] = ['This field is required.']
        self.assertEqual(form.errors, errors)


class TestFormTest(TestCase):
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
        self.personal_stat = LabStats.objects.create(
            human_resource=self.hr,
            created=timezone.now()
        )

    def test_test_form_valid_with_valid_params(self):
        data = {}
        for field in TestForm().fields:
            data[field] = random.randint(1, 100)

        form = TestForm(instance=self.personal_stat, data=data)
        self.assertTrue(form.is_valid())

    def test_test_form_invalid_with_blank(self):
        form = TestForm({})
        self.assertFalse(form.is_valid())
        errors = {}
        for field in TestForm().fields:
            errors[field] = ['This field is required.']
        self.assertEqual(form.errors, errors)
