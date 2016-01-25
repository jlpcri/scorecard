from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.core.urlresolvers import resolve, reverse

from scorecard.apps.personals.models import InnovationStats, LabStats, RequirementStats, TestStats
from scorecard.apps.personals.forms import InnovationForm, LabForm, RequirementForm, TestForm
from scorecard.apps.personals.views import personals, personal_stats
from scorecard.apps.users.models import FunctionalGroup, HumanResource


class PersonalsViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.fg_qi = FunctionalGroup.objects.create(
            name='Quality Innovation',
            key='QI'
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
            user=self.user_superuser,
            manager=True
        )

    def test_personals_url_resolve_to_view(self):
        found = resolve(reverse('personals:personals'))
        self.assertEqual(found.func, personals)

    def test_personals_view_with_no_contents(self):
        response = self.client.get(reverse('personals:personals'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No Contents')
        self.assertQuerysetEqual(response.context['qa_personals'], []),
        self.assertQuerysetEqual(response.context['te_personals'], []),
        self.assertQuerysetEqual(response.context['qi_personals'], []),
        self.assertQuerysetEqual(response.context['re_personals'], []),
        self.assertQuerysetEqual(response.context['tl_personals'], [])

    def test_personals_view_contains_one_tab_per_manager(self):
        response = self.client.get(reverse('personals:personals'))
        self.assertContains(response, '<a href="#quality_innovation" data-toggle="tab">Quality Innovation</a>')
        self.assertNotContains(response, '<a href="#quality_assurance" data-toggle="tab">Quality Assurance</a>')
        self.assertNotContains(response, '<a href="#requirements_engineering" data-toggle="tab">Requirements Engineering</a>')
        self.assertNotContains(response, '<a href="#test_engineering" data-toggle="tab">Test Engineering</a>')
        self.assertNotContains(response, '<a href="#test_lab" data-toggle="tab">Test Lab</a>')

    def test_personals_view_contains_5_tabs_per_superuser(self):
        self.client.logout()
        self.client.login(
            username=self.superuser_account['username'],
            password=self.superuser_account['password']
        )
        response = self.client.get(reverse('personals:personals'))
        self.assertContains(response, '<a href="#quality_innovation" data-toggle="tab">Quality Innovation</a>')
        self.assertContains(response, '<a href="#quality_assurance" data-toggle="tab">Quality Assurance</a>')
        self.assertContains(response, '<a href="#requirements_engineering" data-toggle="tab">Requirements Engineering</a>')
        self.assertContains(response, '<a href="#test_engineering" data-toggle="tab">Test Engineering</a>')
        self.assertContains(response, '<a href="#test_lab" data-toggle="tab">Test Lab</a>')


class PersonalStatsViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.fg_qi = FunctionalGroup.objects.create(
            name='Quality Innovation',
            key='QI'
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
        self.personal_stats = InnovationStats.objects.create(
            human_resource=self.hr
        )

    def test_personal_stats_url_resolve_to_view(self):
        found = resolve(reverse('personals:personal_stats', args=[self.personal_stats.id, ]))
        self.assertEqual(found.func, personal_stats)

    def test_personal_stats_view_return_200(self):
        response = self.client.get(reverse('personals:personal_stats', args=[self.personal_stats.id, ]), follow=True)
        self.assertEqual(response.status_code, 200)

