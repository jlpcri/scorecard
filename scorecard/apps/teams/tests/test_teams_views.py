from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import resolve, reverse

from scorecard.apps.teams.models import TestMetrics
from scorecard.apps.teams.views import teams, metric_detail
from scorecard.apps.users.models import FunctionalGroup, HumanResource


class TeamsViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.fg_qa = FunctionalGroup.objects.create(
            name='Quality Assurance',
            key='QA'
        )
        self.fg_te = FunctionalGroup.objects.create(
            name='Test Engineering',
            key='TE'
        )
        self.fg_qi = FunctionalGroup.objects.create(
            name='Quality Innovation',
            key='QI'
        )
        self.fg_re = FunctionalGroup.objects.create(
            name='Requirment Engineering',
            key='RE'
        )
        self.fg_tl = FunctionalGroup.objects.create(
            name='Test Lab',
            key='TL'
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
            functional_group=self.fg_qa,
            user=self.user_superuser
        )

    def test_teams_url_resolve_to_view(self):
        found = resolve(reverse('teams:teams'))
        self.assertEqual(found.func, teams)

    def test_teams_view_with_no_content(self):
        responses = self.client.get(reverse('teams:teams'))
        self.assertEqual(responses.status_code, 200)
        self.assertContains(responses, 'No Contents')
        self.assertQuerysetEqual(responses.context['qas'], []),
        self.assertQuerysetEqual(responses.context['tes'], []),
        self.assertQuerysetEqual(responses.context['qis'], []),
        self.assertQuerysetEqual(responses.context['res'], []),
        self.assertQuerysetEqual(responses.context['tls'], [])

    def test_teams_view_contains_one_tab_per_manager(self):
        response = self.client.get(reverse('teams:teams'))
        self.assertContains(response, '<a href="#quality_innovation" data-toggle="tab">Quality Innovation</a>')
        self.assertNotContains(response, '<a href="#quality_assurance" data-toggle="tab">Quality Assurance</a>')
        self.assertNotContains(response, '<a href="#requirements_engineering" data-toggle="tab">Requirements Engineering</a>')
        self.assertNotContains(response, '<a href="#test_engineering" data-toggle="tab">Test Engineering</a>')
        self.assertNotContains(response, '<a href="#test_lab" data-toggle="tab">Test Lab</a>')

    def test_teams_view_contains_5_tabs_per_superuser(self):
        self.client.logout()
        self.client.login(
            username=self.superuser_account['username'],
            password=self.superuser_account['password']
        )
        response = self.client.get(reverse('teams:teams'))
        self.assertContains(response, '<a href="#quality_innovation" data-toggle="tab">Quality Innovation</a>')
        self.assertContains(response, '<a href="#quality_assurance" data-toggle="tab">Quality Assurance</a>')
        self.assertContains(response, '<a href="#requirements_engineering" data-toggle="tab">Requirements Engineering</a>')
        self.assertContains(response, '<a href="#test_engineering" data-toggle="tab">Test Engineering</a>')
        self.assertContains(response, '<a href="#test_lab" data-toggle="tab">Test Lab</a>')


class MetricDetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.fg = FunctionalGroup.objects.create(name='QA')
        self.metric = TestMetrics.objects.create(
            functional_group=self.fg
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
            functional_group=self.fg,
            user=self.user,
            manager=True
        )

    def test_metric_detail_url_resolve_to_view(self):
        found = resolve(reverse('teams:metric_detail', args=[self.metric.id, ]))
        self.assertEqual(found.func, metric_detail)

    def test_metric_detail_successful_with_valid_id(self):
        response = self.client.get(reverse('teams:metric_detail', args=[self.metric.id, ])+'?key=QA',
                                   follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.metric.functional_group.name + ' Metric Detail')
        self.assertContains(response, self.metric.created.strftime('%Y-%m-%d'))