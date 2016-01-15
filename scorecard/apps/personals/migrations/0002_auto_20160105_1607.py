# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='innovationstats',
            name='complaints',
        ),
        migrations.RemoveField(
            model_name='innovationstats',
            name='compliments',
        ),
        migrations.RemoveField(
            model_name='innovationstats',
            name='escalations',
        ),
        migrations.RemoveField(
            model_name='labstats',
            name='complaints',
        ),
        migrations.RemoveField(
            model_name='labstats',
            name='compliments',
        ),
        migrations.RemoveField(
            model_name='labstats',
            name='escalations',
        ),
        migrations.RemoveField(
            model_name='requirementstats',
            name='complaints',
        ),
        migrations.RemoveField(
            model_name='requirementstats',
            name='compliments',
        ),
        migrations.RemoveField(
            model_name='requirementstats',
            name='escalations',
        ),
        migrations.RemoveField(
            model_name='teststats',
            name='complaints',
        ),
        migrations.RemoveField(
            model_name='teststats',
            name='compliments',
        ),
        migrations.RemoveField(
            model_name='teststats',
            name='escalations',
        ),
    ]
