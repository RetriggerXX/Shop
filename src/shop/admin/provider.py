from django.contrib import admin
from ..models import (
    Provider
)

class ProviderAdmin(admin.ModelAdmin):
    fields = ("name", "country", "zip_address")
    list_display = ("name", "country", "zip_address")

provider = admin.site.register(Provider, ProviderAdmin)