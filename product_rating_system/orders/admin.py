from django.contrib import admin

from .models import Order, OrdersCart


class OrderAdmin(admin.ModelAdmin):
    list_display = ['cart', 'user_id', 'product_id']


admin.site.register(Order, OrderAdmin)


class OrdersCartAdmin(admin.ModelAdmin):
    list_display = ['id', 'no_of_items', 'no_of_product', 'created_date']


admin.site.register(OrdersCart, OrdersCartAdmin)
