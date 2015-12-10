from django.test import TestCase
from django.contrib.auth.models import User

from scorecard.apps.users.models import FunctionalGroup, HumanResource


class FunctionalGroupModelTest(TestCase):
    def test_string_representations(self):
        functional_group = FunctionalGroup.objects.create(
            name='Test Team Engineering',
            key='TTE'
        )
        self.assertEqual(str(functional_group), '{0}: {1}'.format(functional_group.name, functional_group.key))

    def test_verbose_name_plural(self):
        self.assertEqual(str(FunctionalGroup._meta.verbose_name_plural), 'functional groups')


class HumanResourceModelTest(TestCase):
    def setUp(self):
        self.functional_group = FunctionalGroup.objects.create(
            name='Test Team Engineering',
            key='TTE'
        )
        self.user = User.objects.create(
            username='Test User',
            password='Password'
        )

    def test_string_representations(self):
        human = HumanResource.objects.create(
            functional_group=self.functional_group,
            user=self.user
        )
        self.assertEqual(str(human), '{0}: {1}'.format(human.user.username, human.manager))

    def test_verbose_name_plural(self):
        self.assertEqual(str(HumanResource._meta.verbose_name_plural), 'human resources')