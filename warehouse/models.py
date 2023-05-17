from django.db import models

from catalogue.models import Product


class WarehouseItem(models.Model):
    article = models.CharField(max_length=13)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="warehouse_items")
    quantity = models.PositiveIntegerField()
    income_price = models.DecimalField(max_digits=8, decimal_places=2)
    sale_price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now_add=True)
