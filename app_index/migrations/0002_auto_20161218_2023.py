# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 20:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_index.SpendingsBatch', verbose_name='Batch'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=400, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_index.SpendingsBatch', verbose_name='Batch'),
        ),
    ]
