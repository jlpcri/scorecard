# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0014_auto_20160407_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmetrics',
            name='initiative_time',
            field=models.DecimalField(default=0, verbose_name=b'Initiatives Time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
    ]
