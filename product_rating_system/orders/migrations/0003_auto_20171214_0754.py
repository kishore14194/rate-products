# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-14 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
