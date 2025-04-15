from django.contrib import admin
from ..models import (
    ProductDetail
)



class ProductDetailAdmin(admin.ModelAdmin):
    #fields = ("product", "height", "weight", "description_all")
    fieldsets = [
        (
            "Название товара",
            {
                "fields": ("product",),
            }
        ),
        (
            "Размер товара",
            {
                "fields": ("height","weight"),
            }
        ),
        (
            "Описание",
            {
                "fields": ("description_all",),
            }
        )
    ]
    list_display = ("product", "height", "weight", "description_all")


product_detail = admin.site.register(ProductDetail, ProductDetailAdmin)