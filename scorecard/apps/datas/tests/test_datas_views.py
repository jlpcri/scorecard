from django.contrib.auth.models import User
from django.core.urlresolvers import resolve, reverse
from django.test import TestCase, Client

from scorecard.apps.datas.views import datas, export_excel
from scorecard.apps.users.models import FunctionalGroup, HumanResource


class DatasViewTest(TestCase):
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

    def test_datas_url_resolve_to_view(self):
        found = resolve(reverse('datas:datas'))
        self.assertEqual(found.func, datas)

    def test_datas_view_with_no_content(self):
        response = self.client.get(reverse('datas:datas'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No Contents')

    def test_export_excel_url_resolve_to_view(self):
        found = resolve(reverse('datas:export_excel'))
        self.assertEqual(found.func, export_excel)

    def test_export_excel_view_return_excel_format(self):
        response = self.client.get(reverse('datas:export_excel'))
        self.assertEqual(response['Content-Type'], 'application/vnd.ms-excel')
