# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-13 17:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productrating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productrating',
            name='added_by',
        ),
        migrations.RemoveField(
            model_name='productrating',
            name='product',
        ),
        migrations.DeleteModel(
            name='ProductRating',
        ),
    ]