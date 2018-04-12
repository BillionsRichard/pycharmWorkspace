# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-04 00:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='createTime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='lastTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
