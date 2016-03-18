# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0008_auto_20160122_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innovationmetrics',
            name='avg_team_size',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'average team size'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='delays_introduced_time',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'delays introduced (hours)'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='overtime_weekday',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'weekday overtime'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='overtime_weekend',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'weekend overtime'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='rework_introduced_time',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'rework introduced (hours)'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='sdis_not_prevented',
            field=models.PositiveIntegerField(default=0, verbose_name=b'SDIs not prevented'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='slas_met',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name=b'SLAs met'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='staffs',
            field=models.PositiveIntegerField(default=0, verbose_name=b'staff'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='avg_team_size',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'average team size'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='delays_introduced_time',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'delays introduced (hours)'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='overtime_weekday',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'weekday overtime'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='overtime_weekend',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'weekend overtime'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='rework_introduced_time',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'rework introduced (hours)'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='sdis_not_prevented',
            field=models.PositiveIntegerField(default=0, verbose_name=b'SDIs not prevented'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='slas_met',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name=b'SLAs met'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='staffs',
            field=models.PositiveIntegerField(default=0, verbose_name=b'staff'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='avg_team_size',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'average team size'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='delays_introduced_time',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'delays introduced (hours)'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='overtime_weekday',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'weekday overtime'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='overtime_weekend',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'weekend overtime'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='rework_introduced_time',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'rework introduced (hours)'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='sdis_not_prevented',
            field=models.PositiveIntegerField(default=0, verbose_name=b'SDIs not prevented'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='slas_met',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name=b'SLAs met'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='staffs',
            field=models.PositiveIntegerField(default=0, verbose_name=b'staff'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='avg_team_size',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'average team size'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='avg_time_frame',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'Average time frame'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='defect_caught',
            field=models.PositiveIntegerField(default=0, verbose_name=b'defects caught'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='delays_introduced_time',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'delays introduced (hours)'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='overtime_weekday',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'weekday overtime'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='overtime_weekend',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'weekend overtime'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='rework_introduced_time',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'rework introduced (hours)'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='sdis_not_prevented',
            field=models.PositiveIntegerField(default=0, verbose_name=b'SDIs not prevented'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='slas_met',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name=b'SLAs met'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='staffs',
            field=models.PositiveIntegerField(default=0, verbose_name=b'staff'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_auto_dev',
            field=models.PositiveIntegerField(default=0, verbose_name=b'TCs developed automatically'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_auto_dev_time',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'automated TC development time'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_auto_execution',
            field=models.PositiveIntegerField(default=0, verbose_name=b'TCs automatically executed'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_auto_execution_time',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'automatic TC time savings'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_manual_dev',
            field=models.PositiveIntegerField(default=0, verbose_name=b'TCs manually developed'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_manual_dev_time',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'manual TC development time'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_manual_execution',
            field=models.PositiveIntegerField(default=0, verbose_name=b'TCs manually executed'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_manual_execution_time',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name=b'manual TC execution time'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='uat_defects_not_prevented',
            field=models.PositiveIntegerField(default=0, verbose_name=b'UAT defects not prevented'),
        ),
    ]
