from enum import Enum

from django.db import models


class BasicUnitType(Enum):
    KILOGRAM = "KG"
    PIECE = "PC"
    PACKET = "PKT"
    METER = "MTR"
    UNIT = "UNIT"  # Use this if none of the above matches

    CHOICES = (
        (KILOGRAM, "Kilogram"),
        (PIECE, "Piece"),
        (PACKET, "Packet"),
        (METER, "Meter"),
        (UNIT, "Unit"),
    )


class Product(models.Model):
    """
    A SKU like entity. Any product that the company has that can be counted as inventory can be added here.
    """

    name = models.CharField(max_length=255)
    company = models.ForeignKey(
        "customer.Company", on_delete=models.PROTECT, related_name="products"
    )
    description = models.TextField(null=True, blank=True)
    unit_basic = models.CharField(
        choices=BasicUnitType.CHOICES.value,
        max_length=10,
        default=BasicUnitType.UNIT.value,
    )
    rate = models.BigIntegerField(
        null=True, blank=True, help_text="Rate of the item as per the basic unit"
    )
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    quantity_stock = models.DecimalField(
        decimal_places=3, max_digits=12, null=True, blank=True
    )
    quantity_sold = models.DecimalField(
        decimal_places=3, max_digits=12, null=True, blank=True
    )

    class Meta:
        verbose_name_plural = "products"

    def __str__(self):
        return self.name
