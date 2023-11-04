from django.urls import path
from . import views

urlpatterns = [
    path('play', views.play_sound, name='play_sound'),
    path('play_any', views.play_any_sound, name='play_any_sound'),
]
