# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='automation',
            old_name='column_fields',
            new_name='column_field',
        ),
    ]
