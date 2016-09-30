# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20160411_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectphase',
            name='functional_group',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='functional_group',
        ),
        migrations.AlterField(
            model_name='projectphase',
            name='subteam',
            field=models.ForeignKey(to='users.Subteam'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='subteam',
            field=models.ForeignKey(to='users.Subteam'),
        ),
    ]
