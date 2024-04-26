from django.urls import path
from .views import *

urlpatterns = [
    path('',displayHome,name='dashboard_home')
]