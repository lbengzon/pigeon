# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ridesharing', '0008_auto_20170112_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='time',
        ),
        migrations.AlterField(
            model_name='ride',
            name='date',
            field=models.DateTimeField(),
        ),
    ]