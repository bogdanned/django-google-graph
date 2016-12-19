# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CashSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('name', models.CharField(max_length=400, null=True, verbose_name='Name')),
                ('description', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('amount', models.IntegerField(null=True, verbose_name='Spending Amount')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('spendings_file', models.FileField(upload_to='ing_spendings', verbose_name='ING Spendings File')),
            ],
        ),
        migrations.CreateModel(
            name='EverydaySpendingING',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('description', models.CharField(max_length=5000, verbose_name='Description')),
                ('amount', models.IntegerField(verbose_name='Amount')),
                ('account_credit', models.IntegerField(verbose_name='Account Credit')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlySpending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('name', models.CharField(max_length=400, null=True, verbose_name='Name')),
                ('description', models.CharField(max_length=5000, null=True, verbose_name='Description')),
                ('amount', models.IntegerField(null=True, verbose_name='Spending Amount')),
            ],
        ),
        migrations.CreateModel(
            name='SpendingsBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('spendings_file', models.FileField(upload_to='ing_spendings', verbose_name='ING Spendings File')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_index.SpendingsBatch', verbose_name='Batch')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_index.Category')),
            ],
        ),
        migrations.AddField(
            model_name='everydayspendinging',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_index.SpendingsBatch', verbose_name='Batch Name'),
        ),
        migrations.AddField(
            model_name='everydayspendinging',
            name='categoty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_index.Category'),
        ),
        migrations.AddField(
            model_name='everydayspendinging',
            name='sub_categoty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_index.SubCategory'),
        ),
        migrations.AddField(
            model_name='category',
            name='batch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_index.SpendingsBatch', verbose_name='Batch'),
        ),
    ]
