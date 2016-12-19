# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 21:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_index', '0005_auto_20161218_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='everydayspendinging',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_index.Category'),
        ),
        migrations.AlterField(
            model_name='everydayspendinging',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_index.SubCategory'),
        ),
    ]