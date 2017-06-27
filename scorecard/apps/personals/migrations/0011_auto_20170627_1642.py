# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0010_teststats_initiative_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirementstats',
            name='actual_met',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Actual SLA Met'),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='actual_miss',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Actual SLA Miss'),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='compliments',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Compliments'),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='creep',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Scope Creep'),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='efficiency',
            field=models.FloatField(default=0.0, verbose_name=b'Efficiency'),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='gap_analysis',
            field=models.DecimalField(default=0, verbose_name=b'GAP Analysis Time', max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='optimization_time',
            field=models.DecimalField(default=0, verbose_name=b'Optimization Time', max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='project_actuals',
            field=models.DecimalField(default=0, verbose_name=b"Project Actual's", max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='project_loe',
            field=models.DecimalField(default=0, verbose_name=b"Project LOE'S", max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='project_time',
            field=models.DecimalField(default=0, verbose_name=b'Project Time', max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='srs_detail',
            field=models.DecimalField(default=0, verbose_name=b'SRS Detail Time', max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='srs_initial',
            field=models.DecimalField(default=0, verbose_name=b'SRS Initial Time', max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='survey',
            field=models.FloatField(default=0.0, verbose_name=b'Survey'),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='system_met',
            field=models.PositiveIntegerField(default=0, verbose_name=b'System SLA Met'),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='system_miss',
            field=models.PositiveIntegerField(default=0, verbose_name=b'System SLA Miss'),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='time_initiatives',
            field=models.DecimalField(default=0, verbose_name=b'Initiatives Time', max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='utilization',
            field=models.FloatField(default=0.0, verbose_name=b'Utilization'),
        ),
        migrations.AlterField(
            model_name='requirementstats',
            name='active_projects',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Project WIP'),
        ),
        migrations.AlterField(
            model_name='requirementstats',
            name='revisions',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Rework'),
        ),
        migrations.AlterField(
            model_name='requirementstats',
            name='rework_external_time',
            field=models.DecimalField(default=0, verbose_name=b'Scope Creep Time', max_digits=10, decimal_places=2),
        ),
    ]
