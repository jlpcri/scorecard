# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20151204_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innovationmetrics',
            name='active_projects',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='avg_team_size',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='contractors',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='defects_in_dev',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='delays_introduced_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='documentation_coverage',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=2, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='elicitation_analysis_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='escalations',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='license_cost',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='openings',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='other_savings',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='overtime_weekday',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='overtime_weekend',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='pheme_auto_tests',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='pheme_manual_tests',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='resource_swap',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='resource_swap_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='revisions',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='rework_introduced_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='rework_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='sdis_not_prevented',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='slas_met',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=2, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='staffs',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='story_points_backlog',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='story_points_execution',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='story_points_prep',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='uat_defects_not_prevented',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='unit_tests_coverage',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=2, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='unit_tests_dev',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='visilog_txl_parsed',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='visilog_txl_schema_violation',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='avg_team_size',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='contractors',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='delays_introduced_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='escalations',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='license_cost',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='openings',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='other_savings',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='overtime_weekday',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='overtime_weekend',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='physical_machines',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='power_consumption_ups_a',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='power_consumption_ups_b',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='resource_swap',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='resource_swap_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='rework_introduced_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='rework_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='sdis_not_prevented',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='slas_met',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=2, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='staffs',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='tickets_closed',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='tickets_received',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='virtual_machines',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='active_projects',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='avg_team_size',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='backlog',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='contractors',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='delays_introduced_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='elicitation_analysis_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='escalations',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='license_cost',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='openings',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='other_savings',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='overtime_weekday',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='overtime_weekend',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='resource_swap',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='resource_swap_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='revisions',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='rework_external_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='rework_introduced_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='rework_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='sdis_not_prevented',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='slas_met',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=2, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='slas_missed',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=2, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='staffs',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='team_initiative',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='travel_cost',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='avg_team_size',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='avg_time_frame',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='contractors',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='defect_caught',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='delays_introduced_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='escalations',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='license_cost',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='openings',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='other_savings',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='overtime_weekday',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='overtime_weekend',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='project_backlog',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='project_closed',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='project_execution',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='project_prep',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='resource_swap',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='resource_swap_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='rework_introduced_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='rework_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='sdis_not_prevented',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='slas_met',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=2, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='staffs',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='standards_violated',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_auto_dev',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_auto_dev_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_auto_execution',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_auto_execution_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_manual_dev',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_manual_dev_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_manual_execution',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_manual_execution_time',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='team_initiative',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='ticket_backlog',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='ticket_closed',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='ticket_execution',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='ticket_prep',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='uat_defects_not_prevented',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
