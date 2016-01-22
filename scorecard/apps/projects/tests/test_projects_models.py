from django.contrib.auth.models import User
from django.test import TestCase

from scorecard.apps.projects.models import Project, ProjectPhase, Ticket
from scorecard.apps.users.models import FunctionalGroup, HumanResource


class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            name='Sample Project'
        )

    def test_string_representations(self):
        self.assertEqual(str(self.project), self.project.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Project._meta.verbose_name_plural), 'projects')


class ProjectPhaseModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            name='Sample Project'
        )
        self.fg = FunctionalGroup.objects.create(
            name='Quality Innovation',
            key='QI'
        )
        self.user = User.objects.create(
            username='UserName',
            password='Password'
        )
        self.hr = HumanResource.objects.create(
            functional_group=self.fg,
            user=self.user
        )
        self.project_phase = ProjectPhase.objects.create(
            project=self.project,
            functional_group=self.fg,
            lead=self.hr,
            name='Project Phase',
            key='Project Phase Key'
        )

    def test_string_representations(self):
        self.assertEqual(str(self.project_phase), '{0}: {1}: {2}'.format(self.project_phase.name,
                                                                         self.project_phase.project.name,
                                                                         self.project_phase.functional_group.key))

    def test_verbose_name_plural(self):
        self.assertEqual(str(ProjectPhase._meta.verbose_name_plural), 'project phases')


class TicketModelTest(TestCase):
    def setUp(self):
        self.fg = FunctionalGroup.objects.create(
            name='Quality Innovation',
            key='QI'
        )
        self.user = User.objects.create(
            username='UserName',
            password='Password'
        )
        self.hr = HumanResource.objects.create(
            functional_group=self.fg,
            user=self.user
        )
        self.ticket = Ticket.objects.create(
            functional_group=self.fg,
            lead=self.hr,
            key='Ticket Key'
        )

    def test_string_representations(self):
        self.assertEqual(str(self.ticket), '{0}: {1}: {2}'.format(self.ticket.key,
                                                                  self.ticket.lead.user,
                                                                  self.ticket.functional_group.key))

    def test_verbose_name_plural(self):
        self.assertEqual(str(Ticket._meta.verbose_name_plural), 'tickets')

