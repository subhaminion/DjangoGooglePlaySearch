# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 20:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20171008_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchstring',
            name='amount_of_time_searched',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='searchstring',
            name='searched_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 9, 1, 54, 53, 698103)),
        ),
    ]