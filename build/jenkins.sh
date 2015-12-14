#!/bin/ bash

virtualenv --no-site-packages --clear env
. /usr/local/virtualenvs/scorecard/bin/activate

pip install --download-cache /tmp/kenkins/pip-cache -r requirements/jenkins.txt

 python manage.py jenkins --enable-converage --settings=scorecard.settings.jenkins