# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0017_requirementmetrics_optimization_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirementmetrics',
            name='actual_met',
            field=models.DecimalField(default=0, verbose_name=b'Actual SLA Met', max_digits=3, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='actual_miss',
            field=models.DecimalField(default=0, verbose_name=b'Actual SLA Miss', max_digits=3, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='system_met',
            field=models.DecimalField(default=0, verbose_name=b'System SLA Met', max_digits=3, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='system_miss',
            field=models.DecimalField(default=0, verbose_name=b'System SLA Miss', max_digits=3, decimal_places=2),
        ),
    ]
