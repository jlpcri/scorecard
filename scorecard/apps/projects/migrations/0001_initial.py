# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectPhase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=50)),
                ('key', models.CharField(default=b'', max_length=50)),
                ('estimate_start', models.DateTimeField()),
                ('estimate_end', models.DateTimeField()),
                ('actual_start', models.DateTimeField()),
                ('actual_end', models.DateTimeField()),
                ('functional_group', models.ForeignKey(to='users.FunctionalGroup')),
                ('lead', models.ForeignKey(to='users.HumanResource')),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(default=b'', max_length=50)),
                ('estimate_start', models.DateTimeField()),
                ('estimate_end', models.DateTimeField()),
                ('actual_start', models.DateTimeField()),
                ('actual_end', models.DateTimeField()),
                ('functional_group', models.ForeignKey(to='users.FunctionalGroup')),
                ('lead', models.ForeignKey(to='users.HumanResource')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='projectphase',
            unique_together=set([('project', 'name')]),
        ),
    ]
