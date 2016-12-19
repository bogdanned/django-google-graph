#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class MonthlySpending(models.Model):
    """
    A spending that is fixed monthly
    """
    created = models.DateTimeField(auto_now=False,
                                   auto_now_add=True,
                                   blank=False,
                                   null=False,
                                   verbose_name='Creation Date')
    # Date Event was edited for the last time
    updated = models.DateTimeField(auto_now=True,
                                   auto_now_add=False,
                                   blank=False,
                                   null=False,
                                   verbose_name='Updated')
    # Name of the event
    name = models.CharField(max_length=400,
                            null=True,
                            blank=False,
                            verbose_name='Name')
    # Description
    description = models.CharField(max_length=5000,
                                   null=True,
                                   blank=False,
                                   verbose_name='Description')
    # Spending Amount
    amount = models.IntegerField(null=True,
                                 blank=False,
                                 verbose_name='Spending Amount')


class CashSource(models.Model):
    """
    A cash source.
    """
    created = models.DateTimeField(auto_now=False,
                                   auto_now_add=True,
                                   blank=False,
                                   null=False,
                                   verbose_name='Creation Date')
    # Date Event was edited for the last time
    updated = models.DateTimeField(auto_now=True,
                                   auto_now_add=False,
                                   blank=False,
                                   null=False,
                                   verbose_name='Updated')
    # Name of the event
    name = models.CharField(max_length=400,
                            null=True,
                            blank=False,
                            verbose_name='Name')
    # Description
    description = models.CharField(max_length=5000,
                                   null=True,
                                   blank=False,
                                   verbose_name='Description')
    # Spending Amount
    amount = models.IntegerField(null=True,
                                 blank=False,
                                 verbose_name='Spending Amount')


class SpendingsBatch(models.Model):
    """
    Ing Spending Batch(xls)
    """
    name = models.CharField(max_length=200,
                               null=False,
                               blank=False,
                               )
    created = models.DateTimeField(auto_now=False,
                                   auto_now_add=True,
                                   blank=False,
                                   null=False,
                                   verbose_name='Creation Date')
    # Date Event was edited for the last time
    updated = models.DateTimeField(auto_now=True,
                                   auto_now_add=False,
                                   blank=False,
                                   null=False,
                                   verbose_name='Updated')
    spendings_file = models.FileField(upload_to='ing_spendings', verbose_name="ING Spendings File")


class Category(models.Model):
    """
    Ing Category(xls)
    """
    name = models.CharField(unique=True,
                            max_length=400,
                            null=False,
                            blank=False,
                            )
    created = models.DateTimeField(auto_now=False,
                                   auto_now_add=True,
                                   blank=False,
                                   null=False,
                                   verbose_name='Creation Date')
    # Date Event was edited for the last time
    updated = models.DateTimeField(auto_now=True,
                                   auto_now_add=False,
                                   blank=False,
                                   null=False,
                                   verbose_name='Updated')
    batch = models.ForeignKey(SpendingsBatch,
                              null=True,
                              blank=True,
                              verbose_name="Batch")
    def __unicode__(self):
        return self.name

class SubCategory(models.Model):
    """
    Ing Subcategory(xls)
    """
    name = models.CharField(max_length=400,
                            null=False,
                            blank=False,
                            )
    category = models.ForeignKey(Category)
    created = models.DateTimeField(auto_now=False,
                                   auto_now_add=True,
                                   blank=False,
                                   null=False,
                                   verbose_name='Creation Date')
    # Date Event was edited for the last time
    updated = models.DateTimeField(auto_now=True,
                                   auto_now_add=False,
                                   blank=False,
                                   null=False,
                                   verbose_name='Updated')
    batch = models.ForeignKey(SpendingsBatch,
                              null=True,
                              blank=True,
                              verbose_name="Batch")
    def __unicode__(self):
        return self.name

class EverydaySpendingING(models.Model):
    batch = models.ForeignKey(SpendingsBatch,
                              null=True,
                              blank=True,
                              verbose_name="Batch Name")
    date = models.DateTimeField()
    category = models.ForeignKey(Category, blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, blank=True, null=True)
    description = models.CharField(max_length=5000,
                                   null=False,
                                   blank=False,
                                   verbose_name="Description")
    amount = models.IntegerField(null=False,
                                 blank=False, verbose_name="Amount")
    account_credit = models.IntegerField(null=False, blank=False, verbose_name="Account Credit")

    def __unicode__(self):
        return ("{0}€|{1}").format(self.amount, self.date.date(), self.sub_category)
