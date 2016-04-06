from datetime import datetime
import random
from django.test import TestCase

from scorecard.apps.teams.forms import InnovationForm, RequirementForm, LabForm, TestForm


class InnovationFormTest(TestCase):
    # def test_innovation_form_valid_with_valid_params(self):
    #     data = {}
    #     for field in InnovationForm().fields:
    #         if field in ['unit_tests_coverage', 'slas_met']:
    #             data[field] = round(random.random(), 2)
    #         else:
    #             data[field] = random.randint(1, 100)
    #
    #     print data
    #     form = InnovationForm(data=data)
    #     self.assertTrue(form.is_valid())

    def test_innovation_form_invalid_with_blank_data(self):
        form = InnovationForm({})
        errors = {}
        for field in InnovationForm().fields:
            errors[field] = [u'This field is required.']
        del errors['subteam']

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, errors)


class RequirementFormTest(TestCase):
    def test_requirement_form_valid_with_valid_params(self):
        data = {}
        for field in LabForm().fields:
            if field == 'slas_met':
                data[field] = round(random.random(), 2)
            else:
                data[field] = random.randint(1, 100)
        form = RequirementForm(data=data)
        self.assertTrue(form.is_valid)

    def test_requirement_form_invalid_with_blank(self):
        form = RequirementForm({})
        errors = {}
        for field in RequirementForm().fields:
            errors[field] = ['This field is required.']

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, errors)


class LabFormTest(TestCase):
    def test_lab_form_valid_with_valid_params(self):
        data = {}
        for field in LabForm().fields:
            if field == 'slas_met':
                data[field] = round(random.random(), 2)
            else:
                data[field] = random.randint(1, 100)

        form = LabForm(data=data)
        self.assertTrue(form.is_valid())

    def test_lab_form_invalid_with_blank(self):
        form = LabForm({})
        errors = {}
        for field in LabForm().fields:
            errors[field] = ['This field is required.']

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, errors)


class TestFormTest(TestCase):
    # def test_test_form_valid_with_valid_params(self):
    #     data = {}
    #     for field in TestForm().fields:
    #         if field == 'slas_met':
    #             data[field] = round(random.random(), 2)
    #         else:
    #             data[field] = random.randint(1, 100)
    #     form = TestForm(data=data)
    #     self.assertTrue(form.is_valid())

    def test_test_form_invalid_with_blank(self):
        form = TestForm({})
        errors = {}
        for field in TestForm().fields:
            errors[field] = [u'This field is required.']
        del errors['subteam']

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, errors)
