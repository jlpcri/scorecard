# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import random
from scorecard.apps.users.models import FunctionalGroup


def generate_abbreviation(apps, schema_editor):
    fgs = FunctionalGroup.objects.all()
    for fg in fgs:
        fg.abbreviation = random.choice([chr(i) for i in range(ord('A'), ord('Z'))])
        fg.save()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_functionalgroup_metric_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='functionalgroup',
            name='key',
        ),

        migrations.AddField(
            model_name='functionalgroup',
            name='abbreviation',
            field=models.CharField(default='', max_length=4),
            preserve_default=True
        ),
        migrations.RunPython(generate_abbreviation),
        migrations.AlterField(
            model_name='functionalgroup',
            name='abbreviation',
            field=models.CharField(default='', max_length=4, unique=True),
        ),

        migrations.AlterField(
            model_name='functionalgroup',
            name='metric_type',
            field=models.CharField(choices=[(b'Testing', b'Testing'),
                                            (b'Development', b'Development'),
                                            (b'Requirements', b'Requirements'),
                                            (b'Lab', b'Lab')], default=b'Testing', max_length=13),
        ),
    ]
