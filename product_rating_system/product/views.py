# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import mixins, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
import sys, traceback

from product.commons import get_pro_obj, rating_avg
from .schema import ProductDetailSerializer, ProductRatingSerializer
from .format_data import format_product
from .models import ProductDetail, ProductRating


class ProductList(APIView):
    """ Api to get list of products available"""
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        all_pro_obj = ProductDetail.objects.filter(status=True)
        active_products_list = []
        for one_pro in all_pro_obj:
            active_products = {}
            active_products['product_id'] = one_pro.product_id
            active_products['product_name'] = one_pro.product_name
            active_products['mrp'] = one_pro.mrp
            active_products['rating'] = rating_avg(one_pro)
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

        data = serializer.data

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


class RateProduct(APIView):
    """ Api to rate product bought by user"""
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = json.loads(request.body)

        serializer = ProductRatingSerializer(data=data)
        valid = serializer.is_valid()
        if not valid:
            return HttpResponse((json.dumps({"status": "fail", "data": serializer.errors})),
                                status=status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        pro_id = data.get('product_id')
        rating_val = data.get('rating')
        product_obj = get_pro_obj(pro_id)

        if not product_obj:
            return HttpResponse((json.dumps({"status": "fail", "data": "Invalid Product Id"})),
                                status=status.HTTP_400_BAD_REQUEST)

        try:
            """Checks if user already rated the product"""
            rating_obj = ProductRating.objects.get(product=product_obj, added_by=request.user)
        except ProductRating.DoesNotExist:
            create_rating = ProductRating.objects.create(product=product_obj, rating=rating_val, added_by=request.user)
            create_rating.save()
            return HttpResponse((json.dumps({"status": "success", "data": "Thank You for rating the product"})),
                                status=status.HTTP_200_OK)

        rating_obj.rating = rating_val
        rating_obj.save()
        return HttpResponse(
            (json.dumps({"status": "success", "data": "Thank you ! Rating has been successfully updated"})),
            status=status.HTTP_200_OK)
