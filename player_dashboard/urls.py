from django.urls import path
from .views import *

urlpatterns = [
    path('',displayHome,name='home'),
    path('addplayer/',addPlayer,name='addplayer'),
    path('getplayer/<int:pk>/',getPlayerData,name='getplayer'),
    path('update/<int:pk>/', update_player, name='update_player'),
    path('delete/<int:pk>/', delete_player, name='delete_player'),
]