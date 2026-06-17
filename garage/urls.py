from importlib.resources import path

from django import views

urlpatterns = [
    path('', views.garage_home, name='garage_home'),
    path('add_car/', views.add_car, name='add_car'),
    path('edit_car/<int:car_id>/', views.edit_car, name='edit_car'),
    path('delete_car/<int:car_id>/', views.delete_car, name='delete_car'),
]
