from celery.schedules import crontab

# Celery config
CELERY_ACCEPT_CONTENT = ['pickle', 'json', ]
CELERY_RESULT_BACKEND = 'rpc://'
CELERY_RESULT_PERSISTENT = True
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_TASK_RESULT_EXPIRES = None  # no result is return back

CELERY_ROUTE = {
    'scorecard.apps.teams.tasks.weekly_metric_new': {'queue': 'scorecard_queue'}
}

CELERYBEAT_SCHEDULE = {
    # Execute every Friday of week
    'weekly-add-new-metric': {
        'task': 'scorecard.apps.teams.tasks.weekly_metric_new',
        'schedule': crontab(0, 0, day_of_week='fri'),
        'options': {'queue': 'scorecard_queue'}
    }
}

CELERY_TIMEZONE = 'America/Chicago'
