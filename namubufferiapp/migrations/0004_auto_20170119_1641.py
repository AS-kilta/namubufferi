# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-19 16:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('namubufferiapp', '0003_auto_20170117_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=128, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='namubufferiapp.Product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='account',
            name='magic_token_ttl',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 19, 16, 56, 54, 382548, tzinfo=utc)),
        ),
    ]
