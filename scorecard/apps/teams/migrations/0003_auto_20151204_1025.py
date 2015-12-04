# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_testmetrics_standards_violated'),
    ]

    operations = [
        migrations.AddField(
            model_name='innovationmetrics',
            name='updated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='labmetrics',
            name='updated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='requirementmetrics',
            name='updated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='testmetrics',
            name='updated',
            field=models.BooleanField(default=False),
        ),
    ]
