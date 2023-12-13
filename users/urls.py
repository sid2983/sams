# users/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path("studentRegister", views.student_registration, name="student registration"),
    path("facultyRegister", views.faculty_registration, name="faculty registration"),
    path("registrationSuccess", views.registration_success, name='registration success'),
]
