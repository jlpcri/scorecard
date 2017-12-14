# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0018_auto_20170809_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirementstats',
            name='actual_met',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Actual SLA Met'),
        ),
        migrations.AlterField(
            model_name='requirementstats',
            name='actual_miss',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Actual SLA Miss'),
        ),
        migrations.AlterField(
            model_name='requirementstats',
            name='system_met',
            field=models.PositiveIntegerField(default=0, verbose_name=b'System SLA Met'),
        ),
        migrations.AlterField(
            model_name='requirementstats',
            name='system_miss',
            field=models.PositiveIntegerField(default=0, verbose_name=b'System SLA Miss'),
        ),
    ]
