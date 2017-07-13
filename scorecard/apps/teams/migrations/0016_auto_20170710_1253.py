# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0015_testmetrics_initiative_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirementmetrics',
            name='actual_met',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Actual SLA Met'),
        ),
        migrations.AddField(
            model_name='requirementmetrics',
            name='actual_miss',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Actual SLA Miss'),
        ),
        migrations.AddField(
            model_name='requirementmetrics',
            name='creep',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Scope Creep'),
        ),
        migrations.AddField(
            model_name='requirementmetrics',
            name='gap_analysis',
            field=models.DecimalField(default=0, verbose_name=b'GAP Analysis Time', max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='requirementmetrics',
            name='project_actuals',
            field=models.DecimalField(default=0, verbose_name=b"Project Actual's", max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='requirementmetrics',
            name='project_loe',
            field=models.DecimalField(default=0, verbose_name=b"Project LOE'S", max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='requirementmetrics',
            name='project_time',
            field=models.DecimalField(default=0, verbose_name=b'Project Time', max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='requirementmetrics',
            name='srs_detail',
            field=models.DecimalField(default=0, verbose_name=b'SRS Detail Time', max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='requirementmetrics',
            name='srs_initial',
            field=models.DecimalField(default=0, verbose_name=b'SRS Initial Time', max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='requirementmetrics',
            name='system_met',
            field=models.PositiveIntegerField(default=0, verbose_name=b'System SLA Met'),
        ),
        migrations.AddField(
            model_name='requirementmetrics',
            name='system_miss',
            field=models.PositiveIntegerField(default=0, verbose_name=b'System SLA Miss'),
        ),
        migrations.AddField(
            model_name='requirementmetrics',
            name='time_initiatives',
            field=models.DecimalField(default=0, verbose_name=b'Initiatives Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='active_projects',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Project WIP'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='revisions',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Rework'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='rework_external_time',
            field=models.DecimalField(default=0, verbose_name=b'Scope Creep Time', max_digits=10, decimal_places=2),
        ),
    ]
