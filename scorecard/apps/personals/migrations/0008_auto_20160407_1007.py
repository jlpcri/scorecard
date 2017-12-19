# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0007_auto_20160404_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innovationstats',
            name='customer_facing_time',
            field=models.DecimalField(default=0, verbose_name=b'Customer Facing Time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='innovationstats',
            name='documentation_time',
            field=models.DecimalField(default=0, verbose_name=b'Documentation Time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='innovationstats',
            name='elicitation_analysis_time',
            field=models.DecimalField(default=0, verbose_name=b'Research Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='innovationstats',
            name='overtime_weekday',
            field=models.DecimalField(default=0, verbose_name=b'Overtime Weekday', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='innovationstats',
            name='overtime_weekend',
            field=models.DecimalField(default=0, verbose_name=b'Overtime Weekend', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='innovationstats',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, verbose_name=b'PTO/Holiday Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='innovationstats',
            name='rework_time',
            field=models.DecimalField(default=0, verbose_name=b'Rework Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='innovationstats',
            name='story_points_execution',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Story Points Execution'),
        ),
        migrations.AlterField(
            model_name='innovationstats',
            name='ticketless_dev_time',
            field=models.DecimalField(default=0, verbose_name=b'Ticketless Development Time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='innovationstats',
            name='unit_tests_dev',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Unit Tests Dev'),
        ),
        migrations.AlterField(
            model_name='labstats',
            name='administration_time',
            field=models.DecimalField(default=0, verbose_name=b'Administration hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='labstats',
            name='builds_accepted',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Builds Accepted'),
        ),
        migrations.AlterField(
            model_name='labstats',
            name='builds_submitted',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Builds Submitted'),
        ),
        migrations.AlterField(
            model_name='labstats',
            name='overtime_weekday',
            field=models.DecimalField(default=0, verbose_name=b'Overtime Weekday', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='labstats',
            name='overtime_weekend',
            field=models.DecimalField(default=0, verbose_name=b'Overtime Weekend', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='labstats',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, verbose_name=b'PTO/Holiday Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='labstats',
            name='rework_time',
            field=models.DecimalField(default=0, verbose_name=b'Rework Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='labstats',
            name='ticket_time',
            field=models.DecimalField(default=0, verbose_name=b'Ticket hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='labstats',
            name='tickets_closed',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Ticket Closed'),
        ),
        migrations.AlterField(
            model_name='requirementstats',
            name='elicitation_analysis_time',
            field=models.DecimalField(default=0, verbose_name=b'Research Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementstats',
            name='overtime_weekday',
            field=models.DecimalField(default=0, verbose_name=b'Overtime Weekday', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementstats',
            name='overtime_weekend',
            field=models.DecimalField(default=0, verbose_name=b'Overtime Weekend', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementstats',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, verbose_name=b'PTO/Holiday Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementstats',
            name='revisions',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Revisions'),
        ),
        migrations.AlterField(
            model_name='requirementstats',
            name='rework_external_time',
            field=models.DecimalField(default=0, verbose_name=b'Rework External Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementstats',
            name='rework_time',
            field=models.DecimalField(default=0, verbose_name=b'Rework Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementstats',
            name='travel_cost',
            field=models.DecimalField(default=0, verbose_name=b'Travel Costs', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='defect_caught',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Defects Caught'),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='estimate_auto_time',
            field=models.DecimalField(default=0, verbose_name=b'Estimated Manual Time for Automation', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='loe_deviation',
            field=models.DecimalField(default=0, verbose_name=b'LOE deviation Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='overtime_weekday',
            field=models.DecimalField(default=0, verbose_name=b'Overtime Weekday', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='overtime_weekend',
            field=models.DecimalField(default=0, verbose_name=b'Overtime Weekend', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, verbose_name=b'PTO/Holiday Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='resource_swap_time',
            field=models.DecimalField(default=0, verbose_name=b'Resource Swap Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='rework_time',
            field=models.DecimalField(default=0, verbose_name=b'Rework Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='standard_work_time',
            field=models.DecimalField(default=0, verbose_name=b'Standard Work Time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='standards_violated',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Standards Violated'),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='tc_auto_dev',
            field=models.PositiveIntegerField(default=0, verbose_name=b'TC Auto Dev'),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='tc_auto_dev_time',
            field=models.DecimalField(default=0, verbose_name=b'TC Auto Dev Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='tc_auto_execution',
            field=models.PositiveIntegerField(default=0, verbose_name=b'TC Auto Exec'),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='tc_auto_execution_time',
            field=models.DecimalField(default=0, verbose_name=b'TC Auto Exec Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='tc_manual_dev',
            field=models.PositiveIntegerField(default=0, verbose_name=b'TC Manual Dev'),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='tc_manual_dev_time',
            field=models.DecimalField(default=0, verbose_name=b'TC Manual Dev Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='tc_manual_execution',
            field=models.PositiveIntegerField(default=0, verbose_name=b'TC Manual Exec'),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='tc_manual_execution_time',
            field=models.DecimalField(default=0, verbose_name=b'TC Manual Exec Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='uat_defects_not_prevented',
            field=models.PositiveIntegerField(default=0, verbose_name=b'UAT Defects not Prevented'),
        ),
    ]
