# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0012_remove_requirementstats_efficiency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requirementstats',
            name='utilization',
        ),
        migrations.AlterField(
            model_name='requirementstats',
            name='survey',
            field=models.DecimalField(default=0, verbose_name=b'Survey', max_digits=10, decimal_places=2),
        ),
    ]
