from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('game/', views.game_view, name='game'),
    path('save_score/', views.save_score, name='save_score'),
]
