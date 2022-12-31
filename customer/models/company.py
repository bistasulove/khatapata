from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Company(models.Model):
    name = models.CharField(max_length=255)
    name_legal = models.CharField(
        max_length=255, null=True, blank=True, help_text="Legal business name."
    )
    is_active = models.BooleanField(default=True)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(default="NP", max_length=50)
    website = models.URLField(max_length=255, blank=True)
    email_domain = models.CharField(max_length=255)
    date_established = models.DateField(
        help_text="Date the business was established (yyyy-MM-dd)",
        null=True,
        blank=True,
    )
    business_description = models.TextField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "companies"

    def __str__(self):
        return self.name
