# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectphase',
            name='actual_end',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='projectphase',
            name='actual_start',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='projectphase',
            name='estimate_end',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='projectphase',
            name='estimate_start',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='actual_end',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='actual_start',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='estimate_end',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='estimate_start',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
