from django.shortcuts import render
from .forms import StudentAchievementForm
#import current_user


# Create your views here.
def home(request):
    print(request.user) # this shows user name in terminal when login is done
    return render(request, 'home/home.html', {'title': 'Home'})

def create_achievement(request):
    if request.method == 'POST':
        achievement_form = StudentAchievementForm(request.POST, request.FILES)
        if achievement_form.is_valid():
            achievement_form.save()

    else:
        achievement_form = StudentAchievementForm()

    return render(request, 'home/create_achievement.html', { 'form': achievement_form })
