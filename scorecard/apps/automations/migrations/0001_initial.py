# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

import scorecard.apps.automations.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160127_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tests_run', models.PositiveIntegerField(default=0)),
                ('last_success', models.DateTimeField(auto_now=True, db_index=True)),
                ('last_failure', models.DateTimeField(auto_now=True, db_index=True)),
                ('last_successful_run', models.BooleanField(default=True)),
                ('result', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('script_name', models.TextField(default=b'')),
                ('script_file', models.FileField(null=True, upload_to=scorecard.apps.automations.models.script_location, blank=True)),
                ('column_fields', models.CharField(max_length=50)),
                ('functional_group', models.ForeignKey(to='users.FunctionalGroup')),
            ],
        ),
    ]
