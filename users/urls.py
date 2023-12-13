# users/urls.py

from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("studentRegister/", views.student_registration, name="student_registration"),
    path("facultyRegister/", views.faculty_registration, name="faculty_registration"),
    path("success/", views.registration_success, name="registration_success"),
    path("facultyLogin/", views.faculty_login, name="faculty_login"),
    path("studentLogin/", views.student_login, name="student_login"),
    path("facultyLogout/", views.faculty_logout, name="faculty_logout"),
    path("studentLogout/", views.student_logout, name="student_logout"),
   
]
