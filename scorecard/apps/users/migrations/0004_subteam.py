# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20160127_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subteam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('hourly_rate', models.IntegerField(default=50)),
                ('parent', models.ForeignKey(to='users.FunctionalGroup')),
            ],
        ),
    ]
