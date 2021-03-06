# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-14 07:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('product_id', models.CharField(max_length=100)),
                ('product_quantity', models.TextField(blank=True, null=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.OrdersCart')),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
