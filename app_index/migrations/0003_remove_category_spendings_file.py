# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 20:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_index', '0002_auto_20161218_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='spendings_file',
        ),
    ]
