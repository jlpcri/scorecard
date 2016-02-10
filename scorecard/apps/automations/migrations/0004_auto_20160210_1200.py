# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automations', '0003_auto_20160210_1029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labautomation',
            old_name='column_filed',
            new_name='column_field',
        ),
    ]
