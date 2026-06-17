from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Brand Name')

    def __str__(self):
        return self.name

class CarCatalog(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    name = models.CharField(max_length=100, verbose_name="Model and Generation")
    
    def __str__(self):
        return f"{self.brand.name} - {self.name}"

class UserCar(models.Model):
    FUEL_CHOICES = [ 
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]
    STAGE_CHOICES = [
        ('Stock', 'Stock'),
        ('Stage 1', 'Stage 1'),
        ('Stage 2', 'Stage 2'),
        ('Stage 3', 'Stage 3'),
        ('Stage 4', 'Stage 4'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_cars')
    car_base = models.ForeignKey(CarCatalog, on_delete=models.PROTECT, verbose_name="Enter car model and generation", help_text="Select the car model and generation from the catalog")
    engine = models.CharField(max_length=50, verbose_name="Engine / Modification", help_text="e.g., 340i, M550d")
    year = models.IntegerField(verbose_name="Year of Release")
    fuel_type = models.CharField(max_length=15, choices=FUEL_CHOICES, default='Petrol', verbose_name="Fuel Type")
    stage = models.CharField(max_length=10, choices=STAGE_CHOICES, default='Stock', verbose_name="Tuning Level")
    specs = models.TextField(blank=True, verbose_name="Spec List / Modifications")

    def __str__(self):
        return f"{self.user.username} - {self.car_base.name}"