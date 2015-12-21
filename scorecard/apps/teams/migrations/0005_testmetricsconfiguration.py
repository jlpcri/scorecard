# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
        ('teams', '0004_auto_20151215_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestMetricsConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hours_per_week', models.PositiveSmallIntegerField(default=0)),
                ('costs_per_hour_staff', models.PositiveSmallIntegerField(default=0)),
                ('costs_per_hour_contractor', models.PositiveSmallIntegerField(default=0)),
                ('functional_group', models.ForeignKey(to='users.FunctionalGroup')),
            ],
        ),
    ]
