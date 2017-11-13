# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0016_auto_20170710_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirementmetrics',
            name='optimization_time',
            field=models.DecimalField(default=0, verbose_name=b'Optimization Time', max_digits=10, decimal_places=2),
        ),
    ]
