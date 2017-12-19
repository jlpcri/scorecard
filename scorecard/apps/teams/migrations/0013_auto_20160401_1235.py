# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0012_auto_20160401_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innovationmetrics',
            name='customer_facing_time',
            field=models.DecimalField(default=0, verbose_name=b'Customer facing hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='documentation_time',
            field=models.DecimalField(default=0, verbose_name=b'Documentation hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, verbose_name=b'PTO/Holiday hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='ticketless_dev_time',
            field=models.DecimalField(default=0, verbose_name=b'Ticketless development hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='administration_time',
            field=models.DecimalField(default=0, verbose_name=b'Project hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='project_time',
            field=models.DecimalField(default=0, verbose_name=b'Project hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, verbose_name=b'PTO/Holiday hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='ticket_time',
            field=models.DecimalField(default=0, verbose_name=b'Project hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, verbose_name=b'PTO/Holiday hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='estimate_auto_time',
            field=models.DecimalField(default=0, verbose_name=b'Estimated manual time for automation', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, verbose_name=b'PTO/Holiday hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='standard_work_time',
            field=models.DecimalField(default=0, verbose_name=b'Standard work time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
    ]
