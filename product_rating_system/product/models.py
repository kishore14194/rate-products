from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ProductDetail(models.Model):
    product_id = models.CharField(unique=True, max_length=100, null=False, blank=False)
    product_name = models.CharField(max_length=100, null=False, blank=False)
    product_desc = models.TextField(blank=True, null=True)
    mrp = models.FloatField()
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self.product_name

    class Meta:
        db_table = 'product_detail'


class ProductRating(models.Model):
    product = models.ForeignKey(ProductDetail, blank=False, null=False)
    rating = models.IntegerField(blank=False, null=False)
    comments = models.TextField(blank=True, null=True)
    added_by = models.ForeignKey(User, blank=False, null=False)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'added_by',)
        db_table = 'product_rating'

