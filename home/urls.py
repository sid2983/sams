# sams/urls.py

from django.contrib import admin
from django.urls import path, include
from home.views import *

app_name = "home"

urlpatterns = [
    path('',home,name="home"),
    path('new_achievement', create_achievement, name="create achievement"),
    # Add other app URLs here
]
