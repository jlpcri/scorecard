# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 20:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20160223_1343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='functionalgroup',
            name='metric_type',
        ),
    ]
