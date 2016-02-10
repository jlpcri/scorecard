# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import scorecard.apps.automations.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160127_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='InnovationAutomation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tests_run', models.PositiveIntegerField(default=0)),
                ('last_success', models.DateTimeField(auto_now=True, db_index=True)),
                ('last_failure', models.DateTimeField(auto_now=True, db_index=True)),
                ('last_successful_run', models.BooleanField(default=True)),
                ('result', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('script_name', models.TextField()),
                ('script_file', models.FileField(upload_to=scorecard.apps.automations.models.script_location)),
                ('column_field', models.TextField(default=b'compliments', choices=[(b'compliments', b'Compliments'), (b'complaints', b'Complaints'), (b'escalations', b'Escalations'), (b'story_points_backlog', b'Story Points Backlog'), (b'story_points_prep', b'Story Points Prep'), (b'unit_tests_coverage', b'Unit Tests Coverage'), (b'documentation_coverage', b'Documentation Coverage'), (b'defects_in_dev', b'Defects In Dev'), (b'revisions', b'Revisions'), (b'active_projects', b'Active Projects'), (b'slas_met', b'SLAs Met'), (b'delays_introduced_time', b'Delays Introduced Time'), (b'sdis_not_prevented', b'SDIs Not Prevented'), (b'', b''), (b'resource_swap', b'Resource Swap'), (b'rework_introduced_time', b'Rework Introduced Time'), (b'avg_team_size', b'Average Team Size'), (b'resource_swap_time', b'Resource Swap Time'), (b'license_cost', b'License Cost'), (b'other_savings', b'Other Savings'), (b'pheme_manual_tests', b'Pheme Manual Tests'), (b'pheme_auto_tests', b'Pheme Auto Tests'), (b'visilog_txl_parsed', b'Visilog TXL Parsed'), (b'visilog_txl_schema_violation', b'Visilog TXL Schema Violation')])),
                ('functional_group', models.ForeignKey(to='users.FunctionalGroup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LabAutomation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tests_run', models.PositiveIntegerField(default=0)),
                ('last_success', models.DateTimeField(auto_now=True, db_index=True)),
                ('last_failure', models.DateTimeField(auto_now=True, db_index=True)),
                ('last_successful_run', models.BooleanField(default=True)),
                ('result', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('script_name', models.TextField()),
                ('script_file', models.FileField(upload_to=scorecard.apps.automations.models.script_location)),
                ('column_filed', models.TextField(default=b'compliments', choices=[(b'compliments', b'Compliments'), (b'complaints', b'Complaints'), (b'escalations', b'Escalations'), (b'tickets_received', b'Tickets Received'), (b'virtual_machines', b'Virtual Machines'), (b'physical_machines', b'Physical Machines'), (b'power_consumption_ups_a', b'Power Consumption UPS A'), (b'power_consumption_upb_b', b'Power Consumption UPS B'), (b'license_cost', b'License Cost')])),
                ('functional_group', models.ForeignKey(to='users.FunctionalGroup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequirementAutomation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tests_run', models.PositiveIntegerField(default=0)),
                ('last_success', models.DateTimeField(auto_now=True, db_index=True)),
                ('last_failure', models.DateTimeField(auto_now=True, db_index=True)),
                ('last_successful_run', models.BooleanField(default=True)),
                ('result', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('script_name', models.TextField()),
                ('script_file', models.FileField(upload_to=scorecard.apps.automations.models.script_location)),
                ('column_field', models.TextField(default=b'compliments', choices=[(b'compliments', b'Compliments'), (b'complaints', b'Complaints'), (b'escalations', b'Escalations'), (b'backlog', b'Backlog'), (b'active_projects', b'Active Projects'), (b'team_initiative', b'Team Initiative'), (b'rework_introduced_time', b'Rework Introduced Time'), (b'slas_met', b'SLAs Met'), (b'slas_missed', b'SLAs Missed'), (b'delays_introduced_time', b'Delays Introduced Time')])),
                ('functional_group', models.ForeignKey(to='users.FunctionalGroup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestAutomation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tests_run', models.PositiveIntegerField(default=0)),
                ('last_success', models.DateTimeField(auto_now=True, db_index=True)),
                ('last_failure', models.DateTimeField(auto_now=True, db_index=True)),
                ('last_successful_run', models.BooleanField(default=True)),
                ('result', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('script_name', models.TextField()),
                ('script_file', models.FileField(upload_to=scorecard.apps.automations.models.script_location)),
                ('column_field', models.TextField(default=b'compliments', choices=[(b'compliments', b'Compliments'), (b'complaints', b'Complaints'), (b'escalations', b'Escalations'), (b'team_initiative', b'Team Initiative'), (b'ticket_backlog', b'Ticket Backlog'), (b'ticket_prep', b'Ticket Prep'), (b'ticket_execution', b'Ticket Execution'), (b'ticket_closed', b'Ticket Closed'), (b'project_backlog', b'Project Backlog'), (b'project_prep', b'Project Prep'), (b'project_execution', b'Project Execution'), (b'project_closed', b'Project Closed'), (b'slas_met', b'SLAs Met'), (b'delays_introduced_time', b'Delays Introduced Time'), (b'sdis_not_prevented', b'SDIs Not Prevented'), (b'resource_swap', b'Resource Swap'), (b'rework_introduced_time', b'Rework Introduced Time'), (b'avg_team_size', b'Average Team Size'), (b'avg_time_frame', b'Average Time Frame'), (b'license_cost', b'License Cost'), (b'other_savings', b'Other Savings')])),
                ('functional_group', models.ForeignKey(to='users.FunctionalGroup')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
