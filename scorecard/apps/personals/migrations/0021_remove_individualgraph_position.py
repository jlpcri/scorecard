# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0020_individualgraph'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individualgraph',
            name='position',
        ),
    ]
