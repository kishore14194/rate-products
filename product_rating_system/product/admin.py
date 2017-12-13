from django.contrib import admin

from .models import ProductDetail

class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_name', 'mrp', 'status']

admin.site.register(ProductDetail, ProductDetailAdmin)
