# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0023_teamgraph'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamgraph',
            name='position',
        ),
    ]
