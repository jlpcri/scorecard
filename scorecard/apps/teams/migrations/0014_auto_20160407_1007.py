# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0013_auto_20160401_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innovationmetrics',
            name='ceeq_daily_summaries',
            field=models.PositiveIntegerField(default=0, verbose_name=b'CEEQ Daily Summaries'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='complaints',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Complaint'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='compliments',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Compliment'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='contractors',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Contractor'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='customer_facing_time',
            field=models.DecimalField(default=0, verbose_name=b'Customer Facing Time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='defects_in_dev',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Defects in Dev'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='documentation_time',
            field=models.DecimalField(default=0, verbose_name=b'Documentation Time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='elicitation_analysis_time',
            field=models.DecimalField(default=0, verbose_name=b'Research Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='escalations',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Escalation'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='license_cost',
            field=models.DecimalField(default=0, verbose_name=b'License Cost', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='openings',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Opening'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='other_savings',
            field=models.DecimalField(default=0, verbose_name=b'Other Saving', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='overtime_weekday',
            field=models.DecimalField(default=0, verbose_name=b'Overtime Weekday', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='overtime_weekend',
            field=models.DecimalField(default=0, verbose_name=b'Overtime Weekend', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='pheme_auto_tests',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Pheme Auto Tests'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='pheme_manual_tests',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Pheme Manual Tests'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, verbose_name=b'PTO/Holiday Time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='resource_swap',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Resource Swap'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='resource_swap_time',
            field=models.DecimalField(default=0, verbose_name=b'Resource Swap Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='rework_introduced_time',
            field=models.DecimalField(default=0, verbose_name=b'Rework Introduced Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='rework_time',
            field=models.DecimalField(default=0, verbose_name=b'Rework Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='sdis_not_prevented',
            field=models.PositiveIntegerField(default=0, verbose_name=b'SDIs not Prevented'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='slas_met',
            field=models.DecimalField(default=0, verbose_name=b'SLAs Met', max_digits=3, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='staffs',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Staff'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='story_points_backlog',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Story Points Backlog'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='story_points_execution',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Story Points Exec'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='story_points_prep',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Story Points Prep'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='ticketless_dev_time',
            field=models.DecimalField(default=0, verbose_name=b'Ticketless Development Time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='uat_defects_not_prevented',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Externally Reported Defects'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='unit_tests_coverage',
            field=models.DecimalField(default=0, verbose_name=b'Unit Tests Coverage', max_digits=3, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='unit_tests_dev',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Unit Tests Dev'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='visilog_txl_parsed',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Visilog TXL Parsed'),
        ),
        migrations.AlterField(
            model_name='innovationmetrics',
            name='visilog_txl_schema_violation',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Visilog Schema Violatoin'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='administration_time',
            field=models.DecimalField(default=0, verbose_name=b'Administration Time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='builds_accepted',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Builds Accepted'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='builds_submitted',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Builds Submitted'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='complaints',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Complaint'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='compliments',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Compliment'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='contractors',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Contractor'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='escalations',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Escalation'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='license_cost',
            field=models.DecimalField(default=0, verbose_name=b'License Cost', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='monitor_machines',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Machines under Monitoring'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='openings',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Opening'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='other_savings',
            field=models.DecimalField(default=0, verbose_name=b'Other Saving', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='overtime_weekday',
            field=models.DecimalField(default=0, verbose_name=b'Overtime Weekday', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='overtime_weekend',
            field=models.DecimalField(default=0, verbose_name=b'Overtime Weekend', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='physical_machines',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Physical Machines'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='platform_drift_violations',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Platform Drift Violations'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='project_time',
            field=models.DecimalField(default=0, verbose_name=b'Project Time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, verbose_name=b'PTO/Holiday Time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='resource_swap',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Resource Swap'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='resource_swap_time',
            field=models.DecimalField(default=0, verbose_name=b'Resource Swap Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='rework_introduced_time',
            field=models.DecimalField(default=0, verbose_name=b'Rework Introduced Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='rework_time',
            field=models.DecimalField(default=0, verbose_name=b'Rework Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='sdis_not_prevented',
            field=models.PositiveIntegerField(default=0, verbose_name=b'SDIs not Prevented'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='slas_met',
            field=models.DecimalField(default=0, verbose_name=b'SLAs Met', max_digits=3, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='staffs',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Staff'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='ticket_time',
            field=models.DecimalField(default=0, verbose_name=b'Ticket Time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='tickets_closed',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Tickets Closed'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='tickets_received',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Tickets Received'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='updates_install_docs',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Updates to Install Docs'),
        ),
        migrations.AlterField(
            model_name='labmetrics',
            name='virtual_machines',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Virtual Machines'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='active_projects',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Active Project'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='backlog',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Backlog'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='complaints',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Complaint'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='compliments',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Compliment'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='contractors',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Contractor'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='elicitation_analysis_time',
            field=models.DecimalField(default=0, verbose_name=b'Research Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='escalations',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Escalation'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='license_cost',
            field=models.DecimalField(default=0, verbose_name=b'License Cost', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='openings',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Opening'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='other_savings',
            field=models.DecimalField(default=0, verbose_name=b'Other Saving', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='overtime_weekday',
            field=models.DecimalField(default=0, verbose_name=b'Overtime Weekday', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='overtime_weekend',
            field=models.DecimalField(default=0, verbose_name=b'Overtime Weekend', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, verbose_name=b'PTO/Holiday Time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='resource_swap',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Resource Swap'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='resource_swap_time',
            field=models.DecimalField(default=0, verbose_name=b'Resource Swap Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='revisions',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Revisions'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='rework_external_time',
            field=models.DecimalField(default=0, verbose_name=b'Rework External Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='rework_introduced_time',
            field=models.DecimalField(default=0, verbose_name=b'Rework Introduced Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='rework_time',
            field=models.DecimalField(default=0, verbose_name=b'Rework Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='sdis_not_prevented',
            field=models.PositiveIntegerField(default=0, verbose_name=b'SDIs not Prevented'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='slas_met',
            field=models.DecimalField(default=0, verbose_name=b'SLAs Met', max_digits=3, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='slas_missed',
            field=models.DecimalField(default=0, verbose_name=b'SLAs Missed', max_digits=3, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='staffs',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Staff'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='team_initiative',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Team Initiative'),
        ),
        migrations.AlterField(
            model_name='requirementmetrics',
            name='travel_cost',
            field=models.DecimalField(default=0, verbose_name=b'Travel Costs', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='complaints',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Complaint'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='compliments',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Compliment'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='contractors',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Contractor'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='defect_caught',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Eefects Caught'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='escalations',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Escalation'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='license_cost',
            field=models.DecimalField(default=0, verbose_name=b'License Cost', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='loe_deviation',
            field=models.DecimalField(default=0, verbose_name=b'LOE Deviation Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='openings',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Opening'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='other_savings',
            field=models.DecimalField(default=0, verbose_name=b'Other Saving', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='overtime_weekday',
            field=models.DecimalField(default=0, verbose_name=b'Overtime Weekday', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='overtime_weekend',
            field=models.DecimalField(default=0, verbose_name=b'Overtime Weekend', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='project_backlog',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Project Backlog'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='project_closed',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Project Closed'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='project_execution',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Project Exec'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='project_prep',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Project Prep'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='pto_holiday_time',
            field=models.DecimalField(default=0, verbose_name=b'PTO/Holiday Time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='resource_swap',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Resource Swap'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='resource_swap_time',
            field=models.DecimalField(default=0, verbose_name=b'Resource Swap Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='rework_introduced_time',
            field=models.DecimalField(default=0, verbose_name=b'Rework Introduced Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='rework_time',
            field=models.DecimalField(default=0, verbose_name=b'Rework Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='sdis_not_prevented',
            field=models.PositiveIntegerField(default=0, verbose_name=b'SDIs not Prevented'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='slas_met',
            field=models.DecimalField(default=0, verbose_name=b'SLAs Met', max_digits=3, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='staffs',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Staff'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='standard_work_time',
            field=models.DecimalField(default=0, verbose_name=b'Standard Work Time', max_digits=10, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0'))]),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='standards_violated',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Standards Violated'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_auto_dev',
            field=models.PositiveIntegerField(default=0, verbose_name=b'TC Auto Dev'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_auto_dev_time',
            field=models.DecimalField(default=0, verbose_name=b'TC Auto Dev Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_auto_execution',
            field=models.PositiveIntegerField(default=0, verbose_name=b'TC Auto Exec'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_auto_execution_time',
            field=models.DecimalField(default=0, verbose_name=b'TC Auto Exec Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_manual_dev',
            field=models.PositiveIntegerField(default=0, verbose_name=b'TC Manually Dev'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_manual_dev_time',
            field=models.DecimalField(default=0, verbose_name=b'TC Manually Dev Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_manual_execution',
            field=models.PositiveIntegerField(default=0, verbose_name=b'TC Manually Exec'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='tc_manual_execution_time',
            field=models.DecimalField(default=0, verbose_name=b'TC Manually Exec Time', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='team_initiative',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Team Initiative'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='ticket_backlog',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Ticket Backlog'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='ticket_closed',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Ticket Closed'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='ticket_execution',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Ticket Exec'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='ticket_prep',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Ticket Prep'),
        ),
        migrations.AlterField(
            model_name='testmetrics',
            name='uat_defects_not_prevented',
            field=models.PositiveIntegerField(default=0, verbose_name=b'UAT Defects not Prevented'),
        ),
    ]
