# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-22 11:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180622_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 22, 11, 31, 32, 639009, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 22, 11, 31, 32, 637985, tzinfo=utc)),
        ),
    ]