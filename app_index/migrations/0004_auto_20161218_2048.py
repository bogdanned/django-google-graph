# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 20:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_index', '0003_remove_category_spendings_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='everydayspendinging',
            old_name='categoty',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='everydayspendinging',
            old_name='sub_categoty',
            new_name='sub_category',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='parent',
            new_name='category',
        ),
    ]
