# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import sys, traceback

from product.commons import get_pro_obj, rating_avg
# from .schema import ProductDetailSerializer, ProductRatingSerializer
# from .format_data import format_product
from orders.schema import OrdersCartSerializer
from .models import OrdersCart, Order


class CreateOrder(APIView):
    """ Api to get list of products available"""
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body)
        order_list = data.get('order_list')
        product_quantity = []
        product_value = []
        product_list = []

        for order in order_list:
            pro_id = order.get('product_id')
            pro_quantity = order.get('quantity')

            product_obj = get_pro_obj(pro_id)
            if not product_obj:
                return HttpResponse((json.dumps({"status": "fail", "data": "Invalid Product Id"})),
                                    status=status.HTTP_400_BAD_REQUEST)
            pro_total = int(product_obj.mrp)*pro_quantity

            product_value.append(pro_total)
            product_list.append(product_obj)
            product_quantity.append(pro_quantity)
        try:
            oc_obj = OrdersCart.objects.create(no_of_product=len(product_quantity), no_of_items=sum(product_quantity),
                                               total_value=sum(product_value))
            oc_obj.save()
            for pro in product_list:
                or_obj = Order.objects.create(cart=oc_obj, user_id=request.user.id, product_id=pro.product_id, product_quantity=0)
                or_obj.save()

            return HttpResponse("Success")
        except:
            traceback.print_exc(file=sys.stdout)
            return HttpResponse("fail")