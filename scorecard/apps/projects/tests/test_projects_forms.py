from django.contrib.auth.models import User
from django.test import TestCase

from scorecard.apps.projects.forms import ProjectNewForm, ProjectPhaseNewForm, TicketNewForm
from scorecard.apps.projects.models import Project
from scorecard.apps.users.models import FunctionalGroup, HumanResource


class ProjectNewFormTest(TestCase):
    def test_project_new_form_valid_with_valid_params(self):
        data = {
            'name': 'New Project'
        }
        form = ProjectNewForm(data=data)
        self.assertTrue(form.is_valid())

    def test_project_new_form_invalid_with_blank(self):
        form = ProjectNewForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['This field is required.']
        })


class ProjectPhaseNewFormTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            name='ProjectName'
        )
        self.fg = FunctionalGroup.objects.create(
            name='Quality Innovation',
            key='QI'
        )
        self.user = User.objects.create(
            username='Username',
            password='Password'
        )
        self.hr = HumanResource.objects.create(
            functional_group=self.fg,
            user=self.user,
            manager=True
        )

    def test_project_phase_new_form_valid_with_valid_params(self):
        data = {
            'project': self.project.id,
            'functional_group': self.fg.id,
            'lead': self.hr.id,
            'name': 'Phase Name',
            'key': 'Phase Key'
        }
        form = ProjectPhaseNewForm(data=data)
        self.assertTrue(form.is_valid())

    def test_project_phase_new_form_invalid_with_blank(self):
        form = ProjectPhaseNewForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'project':  ['This field is required.'],
            'functional_group':  ['This field is required.'],
            'lead':  ['This field is required.'],
            'name':  ['This field is required.']
        })


class TicketNewFormTest(TestCase):
    def setUp(self):
        self.fg = FunctionalGroup.objects.create(
            name='Quality Innovation',
            key='QI'
        )
        self.user = User.objects.create(
            username='Username',
            password='Password'
        )
        self.hr = HumanResource.objects.create(
            functional_group=self.fg,
            user=self.user,
            manager=True
        )

    def test_ticket_new_form_valid_with_valid_params(self):
        data = {
            'functional_group': self.fg.id,
            'lead': self.hr.id,
            'key': 'Ticket Key'
        }
        form = TicketNewForm(data=data)
        self.assertTrue(form.is_valid())

    def test_ticket_new_form_invalid_with_blank(self):
        form = TicketNewForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'functional_group': ['This field is required.'],
            'lead': ['This field is required.'],
            'key': ['This field is required.']
        })
