#!/bin/sh

virtualenv --no-site-packages --clear env
. /usr/local/virtualenvs/scorecard/bin/activate

pip install --download-cache /tmp/kenkins/pip-cache -r requirements/jenkins.txt

 python manage.py jenkins --enable-coverage --settings=scorecard.settings.jenkins