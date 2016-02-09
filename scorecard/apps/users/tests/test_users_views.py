from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, resolve
from django.test import TestCase, Client

from scorecard.apps.users.models import FunctionalGroup, HumanResource
from scorecard.apps.users.views import home


class UsersViewTest(TestCase):
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
        self.user = User.objects.create_user(
            username=self.user_account['username'],
            password=self.user_account['password']
        )

    def test_home_url_resolve_to_view(self):
        found = resolve(reverse('users:home'))
        self.assertEqual(found.func, home)

    def test_home_view_without_authenticated_need_login(self):
        response = self.client.get(reverse('users:home'), follow=True)
        self.assertContains(response, 'Please use your Active Directory credentials.')

    def test_home_view_with_authenticated_display_navbar(self):
        self.client.login(
            username=self.user_account['username'],
            password=self.user_account['password']
        )
        self.hr = HumanResource.objects.create(
            functional_group=self.fg_qi,
            user=self.user
        )

        response = self.client.get(reverse('users:home'), follow=True)
        self.assertContains(response, '<li><a href="/scorecard/projects/"><i class="fa fa-sitemap fa-fw"></i> Projects</a> </li>')
        self.assertContains(response, '<li><a href="/scorecard/personals/"><i class="fa fa-area-chart fa-fw"></i>Personal</a> </li>')
        self.assertContains(response, '<li><a href="/scorecard/teams/"><i class="fa fa-weibo fa-fw"></i>Team</a></li>')
        self.assertContains(response, '<li><a href="/scorecard/datas/"><i class="fa fa-pie-chart fa-fw"></i>Data</a> </li>')
        self.assertContains(response, '<li><a href="/scorecard/automations/"><i class="fa fa-table fa-fw"></i>Automation</a> </li>')
        self.assertContains(response, '<li><a href="/scorecard/help/"><i class="fa fa-thumbs-o-up"></i> Help</a> </li>')

