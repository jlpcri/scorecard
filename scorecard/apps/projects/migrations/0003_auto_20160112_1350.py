# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20160112_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectphase',
            name='key',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='projectphase',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='key',
            field=models.CharField(max_length=50),
        ),
    ]
