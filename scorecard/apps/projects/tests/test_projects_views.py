from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.core.urlresolvers import reverse, resolve

from scorecard.apps.projects.models import Project, ProjectPhase, Ticket
from scorecard.apps.projects.forms import ProjectNewForm, ProjectPhaseNewForm, TicketNewForm
from scorecard.apps.projects.views import projects, project_new, project_phase_new, ticket_new
from scorecard.apps.users.models import FunctionalGroup, HumanResource, Subteam


class ProjectViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.fg_qa = FunctionalGroup.objects.create(
            name='Quality Assurance',
            abbreviation='QA'
        )
        self.fg_te = FunctionalGroup.objects.create(
            name='Test Engineering',
            abbreviation='TE'
        )
        self.fg_qi = FunctionalGroup.objects.create(
            name='Quality Engineering',
            abbreviation='QE'
        )
        self.fg_re = FunctionalGroup.objects.create(
            name='Requirements Engineering',
            abbreviation='RE'
        )
        self.fg_tl = FunctionalGroup.objects.create(
            name='Test Lab',
            abbreviation='TL'
        )

        self.user_account = {
            'username': 'UserName',
            'password': 'PassWord'
        }
        self.superuser_account = {
            'username': 'Super User',
            'password': 'Super Password'
        }
        self.user = User.objects.create_user(
            username=self.user_account['username'],
            password=self.user_account['password']
        )
        self.user_superuser = User.objects.create_superuser(
            username=self.superuser_account['username'],
            password=self.superuser_account['password'],
            email=''
        )
        self.client.login(
            username=self.user_account['username'],
            password=self.user_account['password']
        )
        self.hr = HumanResource.objects.create(
            functional_group=self.fg_qi,
            user=self.user,
            manager=True
        )
        self.hr_superuser = HumanResource.objects.create(
            functional_group=self.fg_qi,
            user=self.user_superuser
        )

    def test_projects_url_resolve_to_view(self):
        found = resolve(reverse('projects:projects'))
        self.assertEqual(found.func, projects)

    def test_projects_view_with_no_content(self):
        response = self.client.get(reverse('projects:projects'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No Projects')
        for item in response.context['groups']:
            self.assertQuerysetEqual(item['tickets'], [])
            self.assertQuerysetEqual(item['projects'], [])

    def test_projects_view_contains_one_tab_per_manager(self):
        response = self.client.get(reverse('projects:projects'))
        self.assertContains(response, '<a href="#QE" data-toggle="tab">Quality Engineering</a>')
        self.assertContains(response, '<a href="#QA" data-toggle="tab">Quality Assurance</a>')
        self.assertContains(response, '<a href="#RE" data-toggle="tab">Requirements Engineering</a>')
        self.assertContains(response, '<a href="#TE" data-toggle="tab">Test Engineering</a>')
        self.assertContains(response, '<a href="#TL" data-toggle="tab">Test Lab</a>')

    def test_projects_view_contains_5_tabs_per_superuser(self):
        self.client.logout()
        self.client.login(
            username=self.superuser_account['username'],
            password=self.superuser_account['password']
        )
        response = self.client.get(reverse('projects:projects'))
        self.assertContains(response, '<a href="#QE" data-toggle="tab">Quality Engineering</a>')
        self.assertContains(response, '<a href="#QA" data-toggle="tab">Quality Assurance</a>')
        self.assertContains(response, '<a href="#RE" data-toggle="tab">Requirements Engineering</a>')
        self.assertContains(response, '<a href="#TE" data-toggle="tab">Test Engineering</a>')
        self.assertContains(response, '<a href="#TL" data-toggle="tab">Test Lab</a>')

    def test_projects_view_contains_project_new_form(self):
        response = self.client.get(reverse('projects:projects'))
        form = ProjectNewForm()
        for field in form:
            self.assertContains(response, field.html_name)

    def test_projects_view_contains_project_phase_new_form(self):
        response = self.client.get(reverse('projects:projects'))
        form = ProjectPhaseNewForm()
        for field in form:
            self.assertContains(response, field.html_name)

    def test_projects_view_contains_ticket_new_form(self):
        response = self.client.get(reverse('projects:projects'))
        form = TicketNewForm()
        for field in form:
            self.assertContains(response, field.html_name)


class ProjectNewTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.fg_qa = FunctionalGroup.objects.create(
            name='Quality Assurance',
            abbreviation='QA'
        )
        self.fg_te = FunctionalGroup.objects.create(
            name='Test Engineering',
            abbreviation='TE'
        )
        self.fg_qi = FunctionalGroup.objects.create(
            name='Quality Innovation',
            abbreviation='QI'
        )
        self.fg_re = FunctionalGroup.objects.create(
            name='Requirment Engineering',
            abbreviation='RE'
        )
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
        self.client.login(
            username=self.user_account['username'],
            password=self.user_account['password']
        )
        self.hr = HumanResource.objects.create(
            functional_group=self.fg_qi,
            user=self.user,
            manager=True
        )
        self.small_revenue = 3

    def test_project_new_url_resolve_to_view(self):
        found = resolve(reverse('projects:project_new'))
        self.assertEqual(found.func, project_new)

    def test_project_new_url_returns_status_200(self):
        response = self.client.post(reverse('projects:project_new'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_project_new_valid_with_valid_params(self):
        data = {
            'name': 'New Project',
            'revenue_scale': self.small_revenue
        }
        response = self.client.post(reverse('projects:project_new'), data)
        project = Project.objects.get(name=data['name'])
        self.assertIsNotNone(project)

    def test_project_new_invalid_with_blank(self):
        response = self.client.post(reverse('projects:project_new'), follow=True)
        self.assertContains(response, 'Errors found')


class ProjectPhaseNewTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.project = Project.objects.create(
            name='Example Project'
        )
        self.fg_qa = FunctionalGroup.objects.create(
            name='Quality Assurance',
            abbreviation='QA'
        )
        self.fg_te = FunctionalGroup.objects.create(
            name='Test Engineering',
            abbreviation='TE'
        )
        self.fg_qi = FunctionalGroup.objects.create(
            name='Quality Innovation',
            abbreviation='QI'
        )
        self.subteam = Subteam.objects.create(
            name='QI subteam',
            parent=self.fg_qi,
        )
        self.fg_re = FunctionalGroup.objects.create(
            name='Requirment Engineering',
            abbreviation='RE'
        )
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
        self.client.login(
            username=self.user_account['username'],
            password=self.user_account['password']
        )
        self.hr = HumanResource.objects.create(
            functional_group=self.fg_qi,
            user=self.user,
            manager=True
        )

    def test_project_phase_new_url_resolve_to_view(self):
        found = resolve(reverse('projects:project_phase_new'))
        self.assertEqual(found.func, project_phase_new)

    def test_project_phase_new_url_returns_status_200(self):
        response = self.client.post(reverse('projects:project_phase_new'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_project_phase_new_valid_with_valid_params(self):
        data = {
            'project': self.project.id,
            'subteam': self.subteam.id,
            'lead': self.user.id,
            'name': 'Phase New Name',
            'key': 'Phase New key'
        }
        response = self.client.post(reverse('projects:project_phase_new'), data)
        project_phase = ProjectPhase.objects.get(name=data['name'])
        self.assertIsNotNone(project_phase)

    def test_project_phase_new_invalid_with_blank(self):
        response = self.client.post(reverse('projects:project_phase_new'), follow=True)
        self.assertContains(response, 'Errors found')


class TicketNewTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.fg_qa = FunctionalGroup.objects.create(
            name='Quality Assurance',
            abbreviation='QA'
        )
        self.fg_te = FunctionalGroup.objects.create(
            name='Test Engineering',
            abbreviation='TE'
        )
        self.fg_qi = FunctionalGroup.objects.create(
            name='Quality Innovation',
            abbreviation='QI'
        )
        self.subteam = Subteam.objects.create(
            name='QI subteam',
            parent=self.fg_qi,
        )
        self.fg_re = FunctionalGroup.objects.create(
            name='Requirment Engineering',
            abbreviation='RE'
        )
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
        self.client.login(
            username=self.user_account['username'],
            password=self.user_account['password']
        )
        self.hr = HumanResource.objects.create(
            functional_group=self.fg_qi,
            user=self.user,
            manager=True
        )
        self.revenue_scale = 3

    def test_ticket_new_url_resolve_to_view(self):
        found = resolve(reverse('projects:ticket_new'))
        self.assertEqual(found.func, ticket_new)

    def test_ticket_new_url_returns_status_200(self):
        response = self.client.post(reverse('projects:ticket_new'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_ticket_new_valid_with_valid_params(self):
        data = {
            'subteam': self.subteam.id,
            'lead': self.user.id,
            'key': 'Phase New key',
            'revenue_scale': self.revenue_scale
        }
        response = self.client.post(reverse('projects:ticket_new'), data)
        ticket = Ticket.objects.get(key=data['key'])
        self.assertIsNotNone(ticket)

    def test_ticket_new_invalid_with_blank(self):
        response = self.client.post(reverse('projects:ticket_new'), follow=True)
        self.assertContains(response, 'Errors found')
