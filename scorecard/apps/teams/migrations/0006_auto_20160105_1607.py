# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_testmetricsconfiguration'),
    ]

    operations = [
        migrations.AddField(
            model_name='innovationmetrics',
            name='complaints',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='innovationmetrics',
            name='compliments',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='labmetrics',
            name='complaints',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='labmetrics',
            name='compliments',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='requirementmetrics',
            name='complaints',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='requirementmetrics',
            name='compliments',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='testmetrics',
            name='complaints',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='testmetrics',
            name='compliments',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
