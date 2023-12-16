from django import forms
from django.forms import widgets

from .models import StudentAchievement

class StudentAchievementForm(forms.ModelForm):
    class Meta:
        model = StudentAchievement
        fields = ['event_name', 'achievement_type', 'category', 'venue', 'date', 'title', 'desc', 'role', 'file', 'image_url']

        labels = {
            'event_name': 'Event Name',
            'achievement_type': 'Achievement Type',
            'desc': 'Description of event',
            'role': 'Role',
            'file': 'Certificate attachment',
            'image_url': 'Certificate URL'
        }

        widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'})
        }

class StudentAchievementVerificationForm(forms.ModelForm):
    class Meta:
        model = StudentAchievement
        fields = ['approved']

        labels = {
            'approved': "Approve achievement"
        }