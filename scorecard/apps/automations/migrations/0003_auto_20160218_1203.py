# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automations', '0002_auto_20160210_1624'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='automation',
            unique_together=set([('functional_group', 'column_field')]),
        ),
    ]
