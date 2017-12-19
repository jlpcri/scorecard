from django.contrib.auth.models import User
from django.test import TestCase

from scorecard.apps.projects.forms import (ProjectNewForm, ProjectPhaseNewForm,
                                           TicketNewForm)
from scorecard.apps.projects.models import Project
from scorecard.apps.users.models import FunctionalGroup, HumanResource, Subteam


class ProjectNewFormTest(TestCase):
    def setUp(self):
        self.revenue_scale = 3

    def test_project_new_form_valid_with_valid_params(self):
        data = {
            'name': 'New Project',
            'revenue_scale': self.revenue_scale
        }
        form = ProjectNewForm(data=data)
        self.assertTrue(form.is_valid())

    def test_project_new_form_invalid_with_blank(self):
        form = ProjectNewForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'name': ['This field is required.'],
            'revenue_scale': ['This field is required.']
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
        self.subteam = Subteam.objects.create(
            name='QI subteam',
            parent=self.fg,
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
            'subteam': self.subteam.id,
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
            'subteam':  ['This field is required.'],
            'lead':  ['This field is required.'],
            'name':  ['This field is required.']
        })


class TicketNewFormTest(TestCase):
    def setUp(self):
        self.fg = FunctionalGroup.objects.create(
            name='Quality Innovation',
            key='QI'
        )
        self.subteam = Subteam.objects.create(
            name='QI subteam',
            parent=self.fg,
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
        self.revenue_scale = 3

    def test_ticket_new_form_valid_with_valid_params(self):
        data = {
            'subteam': self.subteam.id,
            'lead': self.hr.id,
            'key': 'Ticket Key',
            'revenue_scale': self.revenue_scale
        }
        form = TicketNewForm(data=data)
        self.assertTrue(form.is_valid())

    def test_ticket_new_form_invalid_with_blank(self):
        form = TicketNewForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'subteam': ['This field is required.'],
            'lead': ['This field is required.'],
            'key': ['This field is required.'],
            'revenue_scale': ['This field is required.']
        })
