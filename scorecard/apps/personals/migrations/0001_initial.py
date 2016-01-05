# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='InnovationStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('confirmed', models.DateTimeField(auto_now=True, db_index=True)),
                ('updated', models.BooleanField(default=False)),
                ('compliments', models.PositiveIntegerField(default=0)),
                ('complaints', models.PositiveIntegerField(default=0)),
                ('escalations', models.PositiveIntegerField(default=0)),
                ('overtime_weekday', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('overtime_weekend', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('rework_time', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('story_points_execution', models.PositiveIntegerField(default=0)),
                ('unit_tests_dev', models.PositiveIntegerField(default=0)),
                ('elicitation_analysis_time', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('human_resource', models.ForeignKey(to='users.HumanResource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LabStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('confirmed', models.DateTimeField(auto_now=True, db_index=True)),
                ('updated', models.BooleanField(default=False)),
                ('compliments', models.PositiveIntegerField(default=0)),
                ('complaints', models.PositiveIntegerField(default=0)),
                ('escalations', models.PositiveIntegerField(default=0)),
                ('overtime_weekday', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('overtime_weekend', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('rework_time', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('tickets_closed', models.PositiveIntegerField(default=0)),
                ('human_resource', models.ForeignKey(to='users.HumanResource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequirementStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('confirmed', models.DateTimeField(auto_now=True, db_index=True)),
                ('updated', models.BooleanField(default=False)),
                ('compliments', models.PositiveIntegerField(default=0)),
                ('complaints', models.PositiveIntegerField(default=0)),
                ('escalations', models.PositiveIntegerField(default=0)),
                ('overtime_weekday', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('overtime_weekend', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('rework_time', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('elicitation_analysis_time', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('revisions', models.PositiveIntegerField(default=0)),
                ('rework_external_time', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('travel_cost', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('human_resource', models.ForeignKey(to='users.HumanResource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('confirmed', models.DateTimeField(auto_now=True, db_index=True)),
                ('updated', models.BooleanField(default=False)),
                ('compliments', models.PositiveIntegerField(default=0)),
                ('complaints', models.PositiveIntegerField(default=0)),
                ('escalations', models.PositiveIntegerField(default=0)),
                ('overtime_weekday', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('overtime_weekend', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('rework_time', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('tc_manual_dev', models.PositiveIntegerField(default=0)),
                ('tc_manual_dev_time', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('tc_manual_execution', models.PositiveIntegerField(default=0)),
                ('tc_manual_execution_time', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('tc_auto_dev', models.PositiveIntegerField(default=0)),
                ('tc_auto_dev_time', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('tc_auto_execution', models.PositiveIntegerField(default=0)),
                ('tc_auto_execution_time', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('defect_caught', models.PositiveIntegerField(default=0)),
                ('uat_defects_not_prevented', models.PositiveIntegerField(default=0)),
                ('standards_violated', models.PositiveIntegerField(default=0)),
                ('human_resource', models.ForeignKey(to='users.HumanResource')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
