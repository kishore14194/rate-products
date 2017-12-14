# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-14 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrdersCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_product', models.IntegerField()),
                ('no_of_items', models.IntegerField()),
                ('total_value', models.IntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'orders_cart',
            },
        ),
    ]
