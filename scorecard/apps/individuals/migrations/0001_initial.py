# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefiningObjectives',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PQInitiatives',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_savings', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('cost_savings', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('systemic_methods', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('defining_objective', models.ForeignKey(to='individuals.DefiningObjectives')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PQProjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_plan_days_late', models.PositiveIntegerField(default=0)),
                ('tc_days_late', models.PositiveIntegerField(default=0)),
                ('tc_manual', models.PositiveIntegerField(default=0)),
                ('tc_auto', models.PositiveIntegerField(default=0)),
                ('requirement_days_late', models.PositiveIntegerField(default=0)),
                ('tc_exec_days_late', models.PositiveIntegerField(default=0)),
                ('tc_exec_manual', models.PositiveIntegerField(default=0)),
                ('tc_exec_auto', models.PositiveIntegerField(default=0)),
                ('sla_escalations', models.PositiveIntegerField(default=0)),
                ('sla_swaps', models.PositiveIntegerField(default=0)),
                ('sla_weekend', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('sla_overtime_hours', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('uat_ceeq', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('uat_defects', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('sdis', models.PositiveIntegerField(default=0)),
                ('standards_violations', models.PositiveIntegerField(default=0)),
                ('rework_introduced_hours', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductQualityIndividual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('confirmed', models.DateTimeField(auto_now=True, db_index=True)),
                ('updated', models.BooleanField(default=False)),
                ('compliments', models.PositiveIntegerField(default=0)),
                ('complaints', models.PositiveIntegerField(default=0)),
                ('escalations', models.PositiveIntegerField(default=0)),
                ('human_resource', models.ForeignKey(to='users.HumanResource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=50)),
                ('functional_group', models.ForeignKey(to='users.FunctionalGroup')),
            ],
        ),
        migrations.CreateModel(
            name='QAInitiatives',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_savings', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('cost_savings', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('systemic_methods', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('defining_objective', models.ForeignKey(to='individuals.DefiningObjectives')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QAProjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_plan_days_late', models.PositiveIntegerField(default=0)),
                ('tc_days_late', models.PositiveIntegerField(default=0)),
                ('tc_manual', models.PositiveIntegerField(default=0)),
                ('tc_auto', models.PositiveIntegerField(default=0)),
                ('requirement_days_late', models.PositiveIntegerField(default=0)),
                ('tc_exec_days_late', models.PositiveIntegerField(default=0)),
                ('tc_exec_manual', models.PositiveIntegerField(default=0)),
                ('tc_exec_auto', models.PositiveIntegerField(default=0)),
                ('sla_escalations', models.PositiveIntegerField(default=0)),
                ('sla_swaps', models.PositiveIntegerField(default=0)),
                ('sla_weekend', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('sla_overtime_hours', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('uat_ceeq', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('uat_defects', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('sdis', models.PositiveIntegerField(default=0)),
                ('standards_violations', models.PositiveIntegerField(default=0)),
                ('rework_introduced_hours', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('quality_engineering_days_late', models.PositiveIntegerField(default=0)),
                ('test_data_request_days_late', models.PositiveIntegerField(default=0)),
                ('project', models.ForeignKey(to='individuals.Projects')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QualityAssuranceIndividual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('confirmed', models.DateTimeField(auto_now=True, db_index=True)),
                ('updated', models.BooleanField(default=False)),
                ('compliments', models.PositiveIntegerField(default=0)),
                ('complaints', models.PositiveIntegerField(default=0)),
                ('escalations', models.PositiveIntegerField(default=0)),
                ('human_resource', models.ForeignKey(to='users.HumanResource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QualityInnovationIndividual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('confirmed', models.DateTimeField(auto_now=True, db_index=True)),
                ('updated', models.BooleanField(default=False)),
                ('compliments', models.PositiveIntegerField(default=0)),
                ('complaints', models.PositiveIntegerField(default=0)),
                ('escalations', models.PositiveIntegerField(default=0)),
                ('human_resource', models.ForeignKey(to='users.HumanResource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequirementsEngineeringIndividual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('confirmed', models.DateTimeField(auto_now=True, db_index=True)),
                ('updated', models.BooleanField(default=False)),
                ('compliments', models.PositiveIntegerField(default=0)),
                ('complaints', models.PositiveIntegerField(default=0)),
                ('escalations', models.PositiveIntegerField(default=0)),
                ('human_resource', models.ForeignKey(to='users.HumanResource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TEInitiatives',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_savings', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('cost_savings', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('systemic_methods', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('defining_objective', models.ForeignKey(to='individuals.DefiningObjectives')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TEProjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_plan_days_late', models.PositiveIntegerField(default=0)),
                ('tc_days_late', models.PositiveIntegerField(default=0)),
                ('tc_manual', models.PositiveIntegerField(default=0)),
                ('tc_auto', models.PositiveIntegerField(default=0)),
                ('requirement_days_late', models.PositiveIntegerField(default=0)),
                ('tc_exec_days_late', models.PositiveIntegerField(default=0)),
                ('tc_exec_manual', models.PositiveIntegerField(default=0)),
                ('tc_exec_auto', models.PositiveIntegerField(default=0)),
                ('sla_escalations', models.PositiveIntegerField(default=0)),
                ('sla_swaps', models.PositiveIntegerField(default=0)),
                ('sla_weekend', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('sla_overtime_hours', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('uat_ceeq', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('uat_defects', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('sdis', models.PositiveIntegerField(default=0)),
                ('standards_violations', models.PositiveIntegerField(default=0)),
                ('rework_introduced_hours', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('project', models.ForeignKey(to='individuals.Projects')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestEngineeringIndividual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('confirmed', models.DateTimeField(auto_now=True, db_index=True)),
                ('updated', models.BooleanField(default=False)),
                ('compliments', models.PositiveIntegerField(default=0)),
                ('complaints', models.PositiveIntegerField(default=0)),
                ('escalations', models.PositiveIntegerField(default=0)),
                ('human_resource', models.ForeignKey(to='users.HumanResource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestLabIndividual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('confirmed', models.DateTimeField(auto_now=True, db_index=True)),
                ('updated', models.BooleanField(default=False)),
                ('compliments', models.PositiveIntegerField(default=0)),
                ('complaints', models.PositiveIntegerField(default=0)),
                ('escalations', models.PositiveIntegerField(default=0)),
                ('human_resource', models.ForeignKey(to='users.HumanResource')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='teprojects',
            name='te_individual',
            field=models.ForeignKey(to='individuals.TestEngineeringIndividual'),
        ),
        migrations.AddField(
            model_name='teinitiatives',
            name='te_individual',
            field=models.ForeignKey(to='individuals.TestEngineeringIndividual'),
        ),
        migrations.AddField(
            model_name='qaprojects',
            name='qa_individual',
            field=models.ForeignKey(to='individuals.QualityAssuranceIndividual'),
        ),
        migrations.AddField(
            model_name='qainitiatives',
            name='qa_individual',
            field=models.ForeignKey(to='individuals.QualityAssuranceIndividual'),
        ),
        migrations.AddField(
            model_name='pqprojects',
            name='pq_individual',
            field=models.ForeignKey(to='individuals.ProductQualityIndividual'),
        ),
        migrations.AddField(
            model_name='pqprojects',
            name='project',
            field=models.ForeignKey(to='individuals.Projects'),
        ),
        migrations.AddField(
            model_name='pqinitiatives',
            name='pq_individual',
            field=models.ForeignKey(to='individuals.ProductQualityIndividual'),
        ),
        migrations.AlterUniqueTogether(
            name='projects',
            unique_together=set([('name', 'functional_group')]),
        ),
    ]
