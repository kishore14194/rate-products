from django.contrib import admin

from .models import ProductDetail, ProductRating


class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_name', 'mrp', 'status']


admin.site.register(ProductDetail, ProductDetailAdmin)


class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ['product', 'rating', 'added_by', 'created_date']


admin.site.register(ProductRating, ProductRatingAdmin)
