from django.urls import path
from . import views

urlpatterns = [
    path('my-garage/', views.my_garage, name='my_garage'),
    path('edit-car/<int:car_id>/', views.edit_car, name='edit_car'),
    path('delete-car/<int:car_id>/', views.delete_car, name='delete_car'),
]
