# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160122_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='columnpreference',
            name='hide_list',
            field=models.CharField(default=b'', max_length=750, blank=True),
        ),
        migrations.AlterField(
            model_name='columnpreference',
            name='table_name',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
