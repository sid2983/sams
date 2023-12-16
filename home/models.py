from django.db import models

from users.models import *

class StudentAchievement(models.Model):
    type_choices = (
        ('1', 'Academic'),
        ('2', 'Non-Academic'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE, unique=False)
    event_name = models.CharField(max_length=255)
    achievement_type = models.CharField(max_length=255, choices=type_choices)
    category = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    date = models.DateField()
    title = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    file = models.FileField(upload_to='achievement_files/')
    image_url = models.URLField()
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(Faculty, on_delete=models.PROTECT, null=True, blank=True)
    is_pending = models.BooleanField(default=True)
