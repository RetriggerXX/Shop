from django.contrib import admin
from django.utils.html import mark_safe
from django.conf import settings

from .provider import provider
from ..models import (
    Product
)

def not_available(modeladmin, request, queryset):
    queryset.update(is_available = False)





class ProductAdmin(admin.ModelAdmin):
    fields = ("name", "description", "price", "count_items", "photo", "provider")
    list_display = ("name", "description", "price", "count_items", "category", "photo", "is_available", "provider")
    list_editable = ("price", "count_items", "is_available")
    list_filter = ("category", "is_available", "provider")
    search_fields = ("name", "description")
    actions = (not_available,)

    def image_preview(self, obj):
        return mark_safe(f'<img src="{settings.STATIC_URL}shop/img/icon.jpg" width="100" />')

    readonly_fields = ("image_preview", )

product = admin.site.register(Product, ProductAdmin)