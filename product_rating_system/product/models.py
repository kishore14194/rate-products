from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ProductDetail(models.Model):
    product_id = models.CharField(unique=True, max_length=100, null=False, blank=False)
    product_name = models.CharField(max_length=100, null=False, blank=False)
    product_desc = models.TextField(blank=True, null=True)
    mrp = models.FloatField()
    status = models.BooleanField(default=True)


    class Meta:
        db_table = 'product_detail'

