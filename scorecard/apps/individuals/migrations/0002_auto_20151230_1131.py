# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
        ('individuals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='definingobjectives',
            name='functional_group',
            field=models.ForeignKey(default=None, to='users.FunctionalGroup'),
        ),
        migrations.AlterUniqueTogether(
            name='definingobjectives',
            unique_together=set([('name', 'functional_group')]),
        ),
    ]
