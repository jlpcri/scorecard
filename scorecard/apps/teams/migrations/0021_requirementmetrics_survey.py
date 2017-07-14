# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0020_auto_20170713_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirementmetrics',
            name='survey',
            field=models.DecimalField(default=0, verbose_name=b'Survey', max_digits=10, decimal_places=2),
        ),
    ]
