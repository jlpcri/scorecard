from django.contrib.auth.models import User
from django.core.urlresolvers import resolve, reverse
from django.test import Client, TestCase

from scorecard.apps.core.views import landing
from scorecard.apps.users.models import FunctionalGroup, HumanResource


class CoreViewsTest(TestCase):
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

    def test_landing_url_resolve_to_view(self):
        found = resolve(reverse('landing'))
        self.assertEqual(found.func, landing)

    def test_landing_returns_200(self):
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)

    def test_landing_without_authenticated(self):
        response = self.client.get(reverse('landing'))
        self.assertContains(response, 'Please use your Active Directory credentials.')

    def test_landing_with_authenticated(self):
        self.client.login(
            username=self.user_account['username'],
            password=self.user_account['password']
        )
        self.hr = HumanResource.objects.create(
            functional_group=self.fg_qi,
            user=self.user,
            manager=True
        )

        response = self.client.get(reverse('landing'), follow=True)
        self.assertNotContains(response, 'Please use your Active Directory credentials.')
        self.assertContains(response, '<li><a href="/scorecard/projects/"><i class="fa fa-sitemap fa-fw"></i> Projects</a> </li>')
        self.assertContains(response, '<li><a href="/scorecard/personals/"><i class="fa fa-area-chart fa-fw"></i> Personal</a> </li>')
        self.assertContains(response, '<li><a href="/scorecard/teams/"><i class="fa fa-weibo fa-fw"></i> Team</a></li>')
        self.assertContains(response, '<li><a href="/scorecard/datas/"><i class="fa fa-pie-chart fa-fw"></i> Data</a> </li>')
        self.assertContains(response, '<li><a href="/scorecard/automations/"><i class="fa fa-table fa-fw"></i> Automation</a> </li>')
        # self.assertContains(response, '<li><a href="/scorecard/help/"><i class="fa fa-thumbs-o-up"></i> Help</a> </li>')
