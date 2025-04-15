from django.contrib import admin
from ..models import (
    ProductOrder
)

class ProductOrderAdmin(admin.ModelAdmin):
    fields = ("order", "product", "detail")
    list_display = ("order", "product", "detail")


product_order = admin.site.register(ProductOrder, ProductOrderAdmin)