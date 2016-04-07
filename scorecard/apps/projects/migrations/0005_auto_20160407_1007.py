# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20160317_1330'),
        ('projects', '0004_auto_20160225_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='revenue_scale',
            field=models.IntegerField(default=3, choices=[(1, b'Greater than 1M'), (2, b'Between 250K and 1M'), (3, b'Less than 250K')]),
        ),
        migrations.AddField(
            model_name='projectphase',
            name='worker',
            field=models.ManyToManyField(related_name='phase_worker', to='users.HumanResource'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='revenue_scale',
            field=models.IntegerField(default=3, choices=[(1, b'Greater than 1M'), (2, b'Between 250K and 1M'), (3, b'Less than 250K')]),
        ),
        migrations.AddField(
            model_name='ticket',
            name='worker',
            field=models.ManyToManyField(related_name='ticket_worker', to='users.HumanResource'),
        ),
        migrations.AlterField(
            model_name='projectphase',
            name='lead',
            field=models.ForeignKey(related_name='phase_lead', to='users.HumanResource'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='lead',
            field=models.ForeignKey(related_name='ticket_lead', to='users.HumanResource'),
        ),
    ]
