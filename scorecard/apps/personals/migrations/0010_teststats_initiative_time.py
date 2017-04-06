# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0009_auto_20161003_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='teststats',
            name='initiative_time',
            field=models.DecimalField(default=0, verbose_name=b'Initiatives Time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
    ]
