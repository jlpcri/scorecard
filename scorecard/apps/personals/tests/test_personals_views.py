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

    def test_personals_url_resolve_to_view(self):
        found = resolve(reverse('personals:personals'))
        self.assertEqual(found.func, personals)

    def test_personals_view_with_no_contents(self):
        response = self.client.get(reverse('personals:personals'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No Contents')

