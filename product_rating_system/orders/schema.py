from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from orders.models import OrdersCart

class OrdersCartSerializer(serializers.ModelSerializer):
    order_list = serializers.ListField(required=True)

    class Meta:
        model = OrdersCart
        fields = '__all__'