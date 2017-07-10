# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0011_auto_20170627_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requirementstats',
            name='efficiency',
        ),
    ]
