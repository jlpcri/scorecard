from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'TEST_NAME': 'test_database.db'
    }
}

INSTALLED_APPS += ('django_jenkins', )

PROJECT_APPS = (
    'scorecard.apps.congregations',
    'scorecard.apps.core',
    'scorecard.apps.exportations',
    'scorecard.apps.help',
    'scorecard.apps.individuals',
    'scorecard.apps.teams',
    'scorecard.apps.users'
)

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
)

TEST_COVERAGE_EXCLUDES_FOLDERS = [
    '/usr/local/*',
    'scrorecard/apps/*/tests/*',
]
