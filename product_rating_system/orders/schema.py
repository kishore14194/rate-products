from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from orders.models import OrdersCart

class OrdersCartSerializer(serializers.ModelSerializer):
    product_id = serializers.CharField(required=True,
                                         min_length=3, trim_whitespace=True)
    quantity = serializers.IntegerField(required=True, min_value=1)

    class Meta:
        model = OrdersCart
        fields = ('product_id', 'quantity')