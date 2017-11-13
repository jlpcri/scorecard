# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0018_auto_20170712_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requirementmetrics',
            name='actual_met',
        ),
        migrations.RemoveField(
            model_name='requirementmetrics',
            name='actual_miss',
        ),
        migrations.RemoveField(
            model_name='requirementmetrics',
            name='creep',
        ),
        migrations.RemoveField(
            model_name='requirementmetrics',
            name='gap_analysis',
        ),
        migrations.RemoveField(
            model_name='requirementmetrics',
            name='optimization_time',
        ),
        migrations.RemoveField(
            model_name='requirementmetrics',
            name='project_actuals',
        ),
        migrations.RemoveField(
            model_name='requirementmetrics',
            name='project_loe',
        ),
        migrations.RemoveField(
            model_name='requirementmetrics',
            name='project_time',
        ),
        migrations.RemoveField(
            model_name='requirementmetrics',
            name='srs_detail',
        ),
        migrations.RemoveField(
            model_name='requirementmetrics',
            name='srs_initial',
        ),
        migrations.RemoveField(
            model_name='requirementmetrics',
            name='system_met',
        ),
        migrations.RemoveField(
            model_name='requirementmetrics',
            name='system_miss',
        ),
        migrations.RemoveField(
            model_name='requirementmetrics',
            name='time_initiatives',
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='active_projects',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Active Project'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='revisions',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Revisions'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='rework_external_time',
            field=models.DecimalField(default=0, verbose_name=b'Rework External Time', max_digits=10, decimal_places=2),
        ),
    ]
