# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_auto_20160105_1607'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='innovationmetrics',
            options={'verbose_name_plural': 'Innovation Metrics'},
        ),
        migrations.AlterModelOptions(
            name='requirementmetrics',
            options={'verbose_name_plural': 'Requirement Metrics'},
        ),
        migrations.AlterModelOptions(
            name='testmetrics',
            options={'verbose_name_plural': 'Test Metrics'},
        ),
    ]
