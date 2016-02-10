# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import scorecard.apps.automations.models


class Migration(migrations.Migration):

    dependencies = [
        ('automations', '0004_auto_20160210_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innovationautomation',
            name='script_file',
            field=models.FileField(null=True, upload_to=scorecard.apps.automations.models.script_location, blank=True),
        ),
        migrations.AlterField(
            model_name='innovationautomation',
            name='script_name',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='labautomation',
            name='script_file',
            field=models.FileField(null=True, upload_to=scorecard.apps.automations.models.script_location, blank=True),
        ),
        migrations.AlterField(
            model_name='labautomation',
            name='script_name',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='requirementautomation',
            name='script_file',
            field=models.FileField(null=True, upload_to=scorecard.apps.automations.models.script_location, blank=True),
        ),
        migrations.AlterField(
            model_name='requirementautomation',
            name='script_name',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='testautomation',
            name='script_file',
            field=models.FileField(null=True, upload_to=scorecard.apps.automations.models.script_location, blank=True),
        ),
        migrations.AlterField(
            model_name='testautomation',
            name='script_name',
            field=models.TextField(default=b''),
        ),
    ]
