from django.contrib import admin

from customer.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "website", "created_date")
    list_filter = ("is_active",)
    ordering = ("name",)
