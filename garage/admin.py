from django.contrib import admin
from .models import Brand, CarCatalog, UserCar

# Register your models here.
admin.site.register(Brand)
admin.site.register(CarCatalog)
admin.site.register(UserCar)