# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
import sys, traceback

from .schema import ProductDetailSerializer
from .format_data import format_product
from .models import ProductDetail


def get_pro_obj(pro_id):
    """Check if product exists"""
    try:
        pro_obj = ProductDetail.objects.get(product_id=pro_id)
    except ProductDetail.DoesNotExist:
        return None

    return pro_obj


class ProductList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        all_pro_obj = ProductDetail.objects.filter(status=True)
        active_products_list = []
        for one_pro in all_pro_obj:
            active_products = {}
            active_products['product_id'] = one_pro.product_id
            active_products['product_name'] = one_pro.product_name
            active_products['mrp'] = one_pro.mrp
            active_products_list.append(active_products)

        product_list = {"status": "success", "data": active_products_list}

        return HttpResponse((json.dumps(product_list)), status=status.HTTP_200_OK)


class ProductAdd(APIView):
    """ Api for admin to add product """
    permission_classes = (IsAuthenticated, IsAdminUser)

    def post(self, request):
        data = json.loads(request.body)

        serializer = ProductDetailSerializer(data=data)
        valid = serializer.is_valid()
        if not valid:
            return HttpResponse((json.dumps({"status": "fail", "data": serializer.errors})),
                                status=status.HTTP_400_BAD_REQUEST)

        try:
            product_detail_obj = format_product(data)
            add_product = ProductDetail(**product_detail_obj)
            add_product.save()
        except:
            traceback.print_exc(file=sys.stdout)
            return HttpResponse((json.dumps({"status": "fail", "data": "Failed to add the Product"})),
                                status=status.HTTP_400_BAD_REQUEST)

        return HttpResponse((json.dumps({"status": "success", "data": "Item added successfully"})),
                            status=status.HTTP_201_CREATED)


class DeleteProduct(APIView):
    """ Api for admin to deactivate product"""
    permission_classes = (IsAuthenticated, IsAdminUser)

    def delete(self, request):
        data = json.loads(request.body)
        pro_id = data.get('product_id')
        product_obj = get_pro_obj(pro_id)

        if not product_obj:
            return HttpResponse((json.dumps({"status": "fail", "data": "Invalid Product Id"})),
                                status=status.HTTP_400_BAD_REQUEST)

        product_obj.status = False
        product_obj.save()
        return HttpResponse((json.dumps({"status": "success", "data": "Item has been successfully deleted"})),
                            status=status.HTTP_200_OK)
