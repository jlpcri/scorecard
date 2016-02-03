from django.contrib.auth.models import User
from django.test import TestCase, Client

from scorecard.apps.users.models import FunctionalGroup, HumanResource
from scorecard.apps.users.views import home


