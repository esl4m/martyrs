# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MartyrsProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, null=True)),
                ('date_of_birth', models.DateTimeField()),
                ('date_of_death', models.DateTimeField()),
                ('cause_of_death', models.CharField(max_length=128, null=True)),
                ('officer_name', models.CharField(max_length=128, null=True)),
                ('governorate', models.CharField(max_length=128, null=True)),
            ],
            options={
                'db_table': 'MartyrsProfile',
            },
        ),
    ]
