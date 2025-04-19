from django.contrib import admin

from .product import product
from ..models import (
    Order,
    ProductOrder,

)

class ProductInline(admin.StackedInline ):
    model = ProductOrder
    autocomplete_fields = ["product"]
    fields = ["product", "price"]
    readonly_fields = ["price"]
    extra = 1

    def price(self, obj):
        if obj.product:
            return obj.product.price





class OrderAdmin(admin.ModelAdmin):
    fields = ("name", "description", "user")
    list_display = ("name", "description", "user",)
    inlines = [ProductInline,]

order = admin.site.register(Order, OrderAdmin)