# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .format_data import format_product
from .models import ProductDetail

class ProductList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        all_pro_obj = ProductDetail.objects.filter(status=True)
        active_products_list = []
        for one_pro in all_pro_obj:
            active_products = {}
            active_products['product_id'] = one_pro.product_id
            active_products['product_name'] = one_pro.product_name
            active_products['mrp'] = one_pro.mrp
            active_products_list.append(active_products)

        product_list = {"status": "success", "data": active_products_list}
        return HttpResponse(json.dumps(product_list))

class ProductAdd(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        data = json.loads(request.body)

        try:
            product_detail_obj = format_product(data)
            add_product = ProductDetail(**product_detail_obj)
            add_product.save()
        except :
            return HttpResponse(json.dumps({"status": "fail", "data": "Failed to add Inventory"}))

        return HttpResponse("added")