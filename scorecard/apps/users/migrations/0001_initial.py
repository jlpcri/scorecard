from __future__ import unicode_literals
from django.db import migrations, models

from django.contrib.auth.models import User
from scorecard.apps.users.models import FunctionalGroup


class Migration(migrations.Migration):


    KEY_CHOICES = (
        ('QA', 'Quality Assurance'),
        ('QI', 'Quality Innovation'),
        ('RE', 'Requirement Engineering'),
        ('TE', 'Test Engineering'),
        ('TL', 'Test Lab')
    )

    dependencies = [
        # ('users', ''),
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionalGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, unique=True, default='')),
                ('key', models.CharField(max_length=10, choices=KEY_CHOICES, default=''))
            ],
        ),

    migrations.CreateModel(
        name='HumanResource',
        fields=[
            ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            # ('name', models.CharField(default=b'', unique=True, max_length=50)),
            ('functional_group', models.ForeignKey(FunctionalGroup, null=True, blank=True)),
            ('user', models.OneToOneField(User)),
            ('manager', models.BooleanField(default=False)),
            ('contractor', models.BooleanField(default=False))
        ],
    ),

]
