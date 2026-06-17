
from importlib.resources import path

from django import views


urlpatterns = [
    path('',views.leaderboard_home, name='leaderboard_home'),
]