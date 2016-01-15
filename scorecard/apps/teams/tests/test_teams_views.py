from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import resolve, reverse

from scorecard.apps.teams.models import InnovationMetrics
from scorecard.apps.teams.views import teams
from scorecard.apps.users.models import FunctionalGroup


class TeamsViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.fg_pq = FunctionalGroup.objects.create(
            name='Product Quality',
            key='PQ'
        )
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
        self.user = User.objects.create_user(
            username=self.user_account['username'],
            password=self.user_account['password']
        )
        self.client.login(
            username=self.user_account['username'],
            password=self.user_account['password']
        )

    def test_teams_url_resolve_to_view(self):
        found = resolve(reverse('teams:teams'))
        self.assertEqual(found.func, teams)

    def test_teams_view_with_no_content(self):
        responses = self.client.get(reverse('teams:teams'))
        self.assertContains(responses, 'No Contents')
        self.assertQuerysetEqual(responses.context['pqs'], []),
        self.assertQuerysetEqual(responses.context['qas'], []),
        self.assertQuerysetEqual(responses.context['tes'], []),
        self.assertQuerysetEqual(responses.context['qis'], []),
        self.assertQuerysetEqual(responses.context['res'], []),
        self.assertQuerysetEqual(responses.context['tls'], [])