from django.db import models
from garage.models import UserCar
# Create your models here.

class RecordLog(models.Model):
    TYPE_CHOICES = [
        ('0-100', '0-100 km/h'),
        ('0-200', '0-200 km/h'),
        ('100-200', '100-200 km/h'),
        ('400m', '400m (1/4 mile)'),
    ]
    user_car = models.ForeignKey(UserCar, on_delete=models.CASCADE, related_name='records')
    test_type = models.CharField(max_length=10, choices=TYPE_CHOICES, verbose_name="Type of measurements")
    time_seconds = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Time (seconds)")
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user_car.user.username} - {self.user_car.car_base.name} - {self.test_type} - {self.time_seconds}s"