# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0008_auto_20160407_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirementstats',
            name='active_projects',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Active Projects'),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='backlog',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Backlog'),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='initiatives',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Team Initiatives'),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='research_time',
            field=models.DecimalField(default=0, verbose_name=b'Research Time', max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='resource_swap_time',
            field=models.DecimalField(default=0, verbose_name=b'Resource Swap Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementstats',
            name='elicitation_analysis_time',
            field=models.DecimalField(default=0, verbose_name=b'Elicitation/Analysis Time', max_digits=10, decimal_places=2),
        ),
    ]
