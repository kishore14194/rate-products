from __future__ import unicode_literals

from django.db import models


class OrdersCart(models.Model):
    no_of_product = models.IntegerField(null=False, blank=False)
    no_of_items = models.IntegerField(null=False, blank=False)
    total_value = models.IntegerField(null=False, blank=False)
    created_date = models.DateField(auto_now_add=True)

    def __int__(self):
        return self.id

    class Meta:
        db_table = 'orders_cart'


class Order(models.Model):
    cart = models.ForeignKey(OrdersCart, blank=False, null=False)
    user_id = models.CharField(max_length=100, null=False, blank=False)
    product_id = models.CharField(max_length=100, null=False, blank=False)
    product_quantity = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        db_table = 'order'

