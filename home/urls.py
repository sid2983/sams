# sams/urls.py

from django.contrib import admin
from django.urls import path, include
from home.views import *

app_name = "home"

urlpatterns = [
    path('',home,name="home"),

    # Add other app URLs here
]
