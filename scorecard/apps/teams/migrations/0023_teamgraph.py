# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20160317_1330'),
        ('teams', '0022_auto_20171107_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamGraph',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('graph_name', models.CharField(default=b'', max_length=50)),
                ('selections', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50, blank=True), size=5), size=5)),
                ('position', models.CharField(max_length=120, blank=True)),
                ('functional_group', models.ForeignKey(to='users.FunctionalGroup')),
            ],
        ),
    ]
