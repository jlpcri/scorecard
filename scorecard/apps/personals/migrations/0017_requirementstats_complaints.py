# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0016_auto_20170713_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirementstats',
            name='complaints',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Compliments'),
        ),
    ]
