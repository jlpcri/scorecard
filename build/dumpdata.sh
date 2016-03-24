#!/bin/bash

source /usr/local/bin/virtualenvwrapper.sh

workon scorecard

./manage.py dumpdata auth > dumpdata/auth.json --settings=scorecard.settings.dev_sliu --indent=4
./manage.py dumpdata users > dumpdata/users.json --settings=scorecard.settings.dev_sliu --indent=4
./manage.py dumpdata personals > dumpdata/personals.json --settings=scorecard.settings.dev_sliu --indent=4
./manage.py dumpdata projects > dumpdata/projects.json --settings=scorecard.settings.dev_sliu --indent=4
./manage.py dumpdata teams > dumpdata/teams.json --settings=scorecard.settings.dev_sliu --indent=4
./manage.py dumpdata automations > dumpdata/automations.json --settings=scorecard.settings.dev_sliu --indent=4




