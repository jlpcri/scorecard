from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.core.urlresolvers import resolve, reverse
from django.utils import timezone

from scorecard.apps.personals.models import InnovationStats, LabStats, RequirementStats, TestStats
from scorecard.apps.personals.forms import InnovationForm, LabForm, RequirementForm, TestForm
from scorecard.apps.personals.views import personals, personal_stats
from scorecard.apps.users.models import FunctionalGroup, HumanResource, Subteam


class PersonalsViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.fg_qa = FunctionalGroup.objects.create(
            name='Quality Assurance',
            abbreviation='QA'
        )
        self.fg_qa_unified = Subteam.objects.create(
            name='unified',
            parent=self.fg_qa
        )

        self.fg_te = FunctionalGroup.objects.create(
            name='Test Engineering',
            abbreviation='TE'
        )
        self.fg_te_unified = Subteam.objects.create(
            name='unified',
            parent=self.fg_te
        )

        self.fg_qi = FunctionalGroup.objects.create(
            name='Quality Engineering',
            abbreviation='QE'
        )
        self.fg_qi_unified = Subteam.objects.create(
            name='unified',
            parent=self.fg_qi
        )

        self.fg_re = FunctionalGroup.objects.create(
            name='Requirements Engineering',
            abbreviation='RE'
        )
        self.fg_re_unified = Subteam.objects.create(
            name='unified',
            parent=self.fg_re
        )

        self.fg_tl = FunctionalGroup.objects.create(
            name='Test Lab',
            abbreviation='TL'
        )
        self.fg_tl_unified = Subteam.objects.create(
            name='unified',
            parent=self.fg_tl
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
        self.hr = HumanResource.objects.create(
            functional_group=self.fg_qi,
            user=self.user,
            manager=True
        )
        self.client.login(
            username=self.user_account['username'],
            password=self.user_account['password']
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

    def test_personals_view_contains_one_tab_per_manager(self):
        response = self.client.get(reverse('personals:personals'))
        self.assertContains(response, '<a href="#QE-unified" data-toggle="pill">unified</a>')
        self.assertContains(response, '<a href="#QA-unified" data-toggle="pill">unified</a>')
        self.assertContains(response, '<a href="#RE-unified" data-toggle="pill">unified</a>')
        self.assertContains(response, '<a href="#TE-unified" data-toggle="pill">unified</a>')
        self.assertContains(response, '<a href="#TL-unified" data-toggle="pill">unified</a>')

    def test_personals_view_contains_5_tabs_per_superuser(self):
        self.client.logout()
        self.client.login(
            username=self.superuser_account['username'],
            password=self.superuser_account['password']
        )
        response = self.client.get(reverse('personals:personals'))
        self.assertContains(response, '<a href="#QE" data-toggle="tab">Quality Engineering</a>')
        self.assertContains(response, '<a href="#QA" data-toggle="tab">Quality Assurance</a>')
        self.assertContains(response, '<a href="#RE" data-toggle="tab">Requirements Engineering</a>')
        self.assertContains(response, '<a href="#TE" data-toggle="tab">Test Engineering</a>')
        self.assertContains(response, '<a href="#TL" data-toggle="tab">Test Lab</a>')


class PersonalStatsViewTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.fg_qi = FunctionalGroup.objects.create(
            name='Quality Innovation',
            abbreviation='QI'
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
            human_resource=self.hr,
            created=timezone.now()
        )

    def test_personal_stats_url_resolve_to_view(self):
        found = resolve(reverse('personals:personal_stats', args=[self.personal_stats.id, ]))
        self.assertEqual(found.func, personal_stats)

    def test_personal_stats_view_return_200(self):
        response = self.client.get(reverse('personals:personal_stats', args=[self.personal_stats.id, ]), follow=True)
        self.assertEqual(response.status_code, 200)

