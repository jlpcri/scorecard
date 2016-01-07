# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personals', '0002_auto_20160105_1607'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='innovationstats',
            options={'ordering': ['human_resource__user__first_name']},
        ),
        migrations.AlterModelOptions(
            name='labstats',
            options={'ordering': ['human_resource__user__first_name']},
        ),
        migrations.AlterModelOptions(
            name='requirementstats',
            options={'ordering': ['human_resource__user__first_name']},
        ),
        migrations.AlterModelOptions(
            name='teststats',
            options={'ordering': ['human_resource__user__first_name']},
        ),
    ]
