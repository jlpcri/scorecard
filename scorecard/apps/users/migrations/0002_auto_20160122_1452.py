# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColumnPreference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('table_name', models.CharField(default=b'change me', max_length=250)),
                ('hide_list', models.CharField(default=b'', max_length=50, blank=True)),
                ('user', models.ForeignKey(to='auth.User')),
            ],
            options={
                'ordering': ('user',),
                'verbose_name': 'Column Preference',
            },
        ),
        migrations.AlterModelOptions(
            name='functionalgroup',
            options={'verbose_name_plural': 'Functional Groups'},
        ),
    ]
