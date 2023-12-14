from django.db import models

from users.models import *

class StudentAchievement(models.Model):
    type_choices = (
        ('1', 'Academic'),
        ('2', 'Non-Academic'),
    )
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=255)
    achievement_type = models.CharField(max_length=255, choices=type_choices)
    category = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    date = models.DateField()
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    file = models.FileField(upload_to='achievement_files/')
    pic = models.ImageField(upload_to="achievement_pics/")
    approved = models.BooleanField()
    approved_by = models.OneToOneField(Faculty, on_delete=models.PROTECT)
