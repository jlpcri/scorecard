# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automations', '0004_auto_20160329_1533'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='automation',
            unique_together=set([('subteam', 'column_field'), ('human_resource', 'column_field')]),
        ),
        migrations.RemoveField(
            model_name='automation',
            name='functional_group',
        ),
    ]
