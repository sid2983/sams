# sams/urls.py

from django.contrib import admin
from django.urls import path, include
from home.views import *

app_name = "home"

urlpatterns = [
    path('',home,name="home"),
    path('new_achievement/', create_achievement, name="create achievement"),
    path('pendingAchievements/', view_pending, name="pending achievements"),
    path('achievementDetails/<int:achievement_id>/', view_details, name='achievement details'),
    path('achievements/', view_all, name="achievments view"),
    path('verifyachievement/<int:achievement_id>/', verify_achievement, name='achievement verification')

    # Add other app URLs here
]
