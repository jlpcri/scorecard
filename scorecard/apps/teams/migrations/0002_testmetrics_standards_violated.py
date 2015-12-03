# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmetrics',
            name='standards_violated',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
        ),
    ]
