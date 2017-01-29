# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-29 16:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('namubufferiapp', '0005_auto_20170120_2302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='account',
            name='magic_token_ttl',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 29, 16, 54, 32, 194000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='namubufferiapp.Account'),
        ),
    ]
