# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20160317_1330'),
        ('automations', '0003_auto_20160218_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='automation',
            name='human_resource',
            field=models.ForeignKey(blank=True, to='users.HumanResource', null=True),
        ),
        migrations.AddField(
            model_name='automation',
            name='subteam',
            field=models.ForeignKey(blank=True, to='users.Subteam', null=True),
        ),
    ]
