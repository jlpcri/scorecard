# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0003_auto_20160107_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='teststats',
            name='resource_swap_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
        ),
    ]
