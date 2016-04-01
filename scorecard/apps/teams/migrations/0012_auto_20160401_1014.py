# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0011_auto_20160303_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='innovationmetrics',
            name='active_projects',
        ),
        migrations.RemoveField(
            model_name='innovationmetrics',
            name='avg_team_size',
        ),
        migrations.RemoveField(
            model_name='innovationmetrics',
            name='delays_introduced_time',
        ),
        migrations.RemoveField(
            model_name='innovationmetrics',
            name='documentation_coverage',
        ),
        migrations.RemoveField(
            model_name='innovationmetrics',
            name='revisions',
        ),
        migrations.RemoveField(
            model_name='labmetrics',
            name='avg_team_size',
        ),
        migrations.RemoveField(
            model_name='labmetrics',
            name='delays_introduced_time',
        ),
        migrations.RemoveField(
            model_name='requirementmetrics',
            name='avg_team_size',
        ),
        migrations.RemoveField(
            model_name='requirementmetrics',
            name='delays_introduced_time',
        ),
        migrations.RemoveField(
            model_name='testmetrics',
            name='avg_team_size',
        ),
        migrations.RemoveField(
            model_name='testmetrics',
            name='avg_time_frame',
        ),
        migrations.RemoveField(
            model_name='testmetrics',
            name='delays_introduced_time',
        ),
        migrations.AddField(
            model_name='innovationmetrics',
            name='ceeq_daily_summaries',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='innovationmetrics',
            name='customer_facing_time',
            field=models.DecimalField(default=0, verbose_name=b'Customer facing hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01000000000000000020816681711721685132943093776702880859375'))]),
        ),
        migrations.AddField(
            model_name='innovationmetrics',
            name='documentation_time',
            field=models.DecimalField(default=0, verbose_name=b'Documentation hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01000000000000000020816681711721685132943093776702880859375'))]),
        ),
        migrations.AddField(
            model_name='innovationmetrics',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, verbose_name=b'PTO/Holiday hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01000000000000000020816681711721685132943093776702880859375'))]),
        ),
        migrations.AddField(
            model_name='innovationmetrics',
            name='ticketless_dev_time',
            field=models.DecimalField(default=0, verbose_name=b'Ticketless development hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01000000000000000020816681711721685132943093776702880859375'))]),
        ),
        migrations.AddField(
            model_name='labmetrics',
            name='administration_time',
            field=models.DecimalField(default=0, verbose_name=b'Project hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01000000000000000020816681711721685132943093776702880859375'))]),
        ),
        migrations.AddField(
            model_name='labmetrics',
            name='builds_accepted',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='labmetrics',
            name='builds_submitted',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='labmetrics',
            name='monitor_machines',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Machines under monitoring'),
        ),
        migrations.AddField(
            model_name='labmetrics',
            name='platform_drift_violations',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='labmetrics',
            name='project_time',
            field=models.DecimalField(default=0, verbose_name=b'Project hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01000000000000000020816681711721685132943093776702880859375'))]),
        ),
        migrations.AddField(
            model_name='labmetrics',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, verbose_name=b'PTO/Holiday hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01000000000000000020816681711721685132943093776702880859375'))]),
        ),
        migrations.AddField(
            model_name='labmetrics',
            name='ticket_time',
            field=models.DecimalField(default=0, verbose_name=b'Project hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01000000000000000020816681711721685132943093776702880859375'))]),
        ),
        migrations.AddField(
            model_name='labmetrics',
            name='updates_install_docs',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Updates to install documents'),
        ),
        migrations.AddField(
            model_name='requirementmetrics',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, verbose_name=b'PTO/Holiday hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01000000000000000020816681711721685132943093776702880859375'))]),
        ),
        migrations.AddField(
            model_name='testmetrics',
            name='estimate_auto_time',
            field=models.DecimalField(default=0, verbose_name=b'Estimated manual time for automation', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01000000000000000020816681711721685132943093776702880859375'))]),
        ),
        migrations.AddField(
            model_name='testmetrics',
            name='loe_deviation',
            field=models.DecimalField(default=0, verbose_name=b'LOE deviation (hours)', max_digits=10, decimal_places=2),
        ),
        migrations.AddField(
            model_name='testmetrics',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, verbose_name=b'PTO/Holiday hours', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01000000000000000020816681711721685132943093776702880859375'))]),
        ),
        migrations.AddField(
            model_name='testmetrics',
            name='standard_work_time',
            field=models.DecimalField(default=0, verbose_name=b'Standard work time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.01000000000000000020816681711721685132943093776702880859375'))]),
        ),
        migrations.AddField(
            model_name='testmetrics',
            name='testers',
            field=models.PositiveIntegerField(default=0, verbose_name=b'tester'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='elicitation_analysis_time',
            field=models.DecimalField(default=0, verbose_name=b'Research hours', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='uat_defects_not_prevented',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Externally reported defects'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='power_consumption_ups_a',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Power Consumption UPS A'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='power_consumption_ups_b',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Power Consumption UPS B'),
        ),
    ]
