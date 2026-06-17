
from django.urls import path
from . import views

urlpatterns = [
    path('', views.leaderboard_view, name='car_leaderboard'),
]