# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20160407_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='revenue_scale',
            field=models.IntegerField(default=3, choices=[(1, b'Greater than 1M'), (2, b'Between 250K and 1M'), (3, b'Less than 250K'), (4, b'Internal')]),
        ),
        migrations.AlterField(
            model_name='projectphase',
            name='worker',
            field=models.ManyToManyField(related_name='phase_worker', to='users.HumanResource', blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='revenue_scale',
            field=models.IntegerField(default=3, choices=[(1, b'Greater than 1M'), (2, b'Between 250K and 1M'), (3, b'Less than 250K'), (4, b'Internal')]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='worker',
            field=models.ManyToManyField(related_name='ticket_worker', to='users.HumanResource', blank=True),
        ),
    ]
