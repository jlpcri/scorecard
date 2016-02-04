#!/bin/bash

source /usr/local/bin/virtualenvwrapper.sh

workon scorecard

./manage.py loaddata  dumpdata/auth.json --settings=scorecard.settings.dev_sliu
./manage.py loaddata  dumpdata/users.json --settings=scorecard.settings.dev_sliu
./manage.py loaddata  dumpdata/personals.json --settings=scorecard.settings.dev_sliu
./manage.py loaddata  dumpdata/projects.json --settings=scorecard.settings.dev_sliu
./manage.py loaddata  dumpdata/teams.json --settings=scorecard.settings.dev_sliu

