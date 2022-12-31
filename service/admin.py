from django.contrib import admin

from service.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "unit_basic", "rate", "description")
    list_filter = ("is_active",)
