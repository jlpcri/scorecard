# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0006_auto_20160321_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='innovationstats',
            name='customer_facing_time',
            field=models.DecimalField(default=0, verbose_name=b'Customer facing hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AddField(
            model_name='innovationstats',
            name='documentation_time',
            field=models.DecimalField(default=0, verbose_name=b'Documentation hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AddField(
            model_name='innovationstats',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='innovationstats',
            name='ticketless_dev_time',
            field=models.DecimalField(default=0, verbose_name=b'Ticketless development hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AddField(
            model_name='labstats',
            name='administration_time',
            field=models.DecimalField(default=0, verbose_name=b'Project hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AddField(
            model_name='labstats',
            name='builds_accepted',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='labstats',
            name='builds_submitted',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='labstats',
            name='project_time',
            field=models.DecimalField(default=0, verbose_name=b'Project hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AddField(
            model_name='labstats',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='labstats',
            name='ticket_time',
            field=models.DecimalField(default=0, verbose_name=b'Project hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AddField(
            model_name='labstats',
            name='updates_install_docs',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Updates to install documents'),
        ),
        migrations.AddField(
            model_name='requirementstats',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='teststats',
            name='estimate_auto_time',
            field=models.DecimalField(default=0, verbose_name=b'Estimated manual time for automation', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AddField(
            model_name='teststats',
            name='loe_deviation',
            field=models.DecimalField(default=0, verbose_name=b'LOE deviation (hours)', max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='teststats',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='teststats',
            name='standard_work_time',
            field=models.DecimalField(default=0, verbose_name=b'Standard work time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
    ]
