# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_auto_20160122_0911'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='labmetrics',
            options={'verbose_name_plural': 'Lab Metrics'},
        ),
    ]
