# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0017_requirementstats_complaints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirementstats',
            name='complaints',
            field=models.PositiveIntegerField(default=0, verbose_name=b'Complaints'),
        ),
    ]
