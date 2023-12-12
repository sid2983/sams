from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# users/models.py




class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    portfolio_links = models.URLField(max_length=200, blank=True)
    department = models.CharField(max_length=100, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    # Add any common fields here

    def __str__(self):
        return self.username
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add additional fields for student profile
    enrollment_number = models.CharField(max_length=20)
    batch_year = models.IntegerField()
    semester = models.IntegerField()
    section = models.CharField(max_length=10)
    shift = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


class Faculty(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add additional fields for faculty profile
    employee_id = models.CharField(max_length=20, unique=True)
    shift = models.CharField(max_length=10)
    designation = models.CharField(max_length=100)


    def __str__(self):
        return self.user.username