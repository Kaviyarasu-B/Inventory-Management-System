from django.db import models
from django.utils import timezone

class Location(models.Model):
    location_id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductMovement(models.Model):
    movement_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(default=timezone.now)
    from_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='from_movements')
    to_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='to_movements')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()

    def __str__(self):
        return f"Movement ID: {self.movement_id} - {self.product.name}"
