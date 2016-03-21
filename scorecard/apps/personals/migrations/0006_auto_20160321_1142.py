# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0005_auto_20160317_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='innovationstats',
            name='created',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='labstats',
            name='created',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='requirementstats',
            name='created',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='teststats',
            name='created',
            field=models.DateTimeField(db_index=True),
        ),
    ]
