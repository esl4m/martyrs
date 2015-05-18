# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('martyrs_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='martyrsprofile',
            name='cause_of_death',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='martyrsprofile',
            name='governorate',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='martyrsprofile',
            name='officer_name',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
