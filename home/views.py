from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import StudentAchievementForm
from users.models import Student
from .models import StudentAchievement
#import current_user


# Create your views here.
def home(request):
    print(request.user) # this shows user name in terminal when login is done
    return render(request, 'home/home.html', {'title': 'Home'})

@login_required(login_url="/users/studentLogin/")
def create_achievement(request):
    if request.method == 'POST':
        achievement_form = StudentAchievementForm(request.POST, request.FILES)
        stu = Student.objects.get(user=request.user)
        print(stu)
        print(type(stu))
        if achievement_form.is_valid():
            achievement = achievement_form.save(commit=False)
            achievement.student = stu
            achievement.save()

    else:
        achievement_form = StudentAchievementForm()

    return render(request, 'home/create_achievement.html', { 'form': achievement_form })


def view_pending(request):
    pending = StudentAchievement.objects.filter(approved=0)
    
    return render(request, 'home/pending_achievements.html', {'pending': pending})

def view_details(request, achievement_id):
    achievement = StudentAchievement.objects.get(id=achievement_id)
    if achievement.approved_by == None:
        approved_by = "NOT APPROVED"
    else:
        approved_by = achievement.approved_by.user.first_name + achievement.approved_by.user.last_name

    achievement_type = 'Academic' if achievement.achievement_type == '1' else 'Non-academic'
    details = [
        ('Student Name', achievement.student.user.first_name + achievement.student.user.last_name ),
        ('Event Name', achievement.event_name),
        ('Achievement Type', achievement_type),
        ('Category', achievement.category),
        ('Venue', achievement.venue),
        ('Date', achievement.date),
        ('Title', achievement.title),
        ('Description', achievement.desc),
        ('Role', achievement.role),
        ('File', achievement.file),
        ('Image URL', achievement.image_url),
        ('Approval status', achievement.approved),
        ('Approved by', approved_by),
    ]

    return render(request, "home/achievement_details.html", {'achievement_details': details})

def view_all(request):
    achievements = StudentAchievement.objects.filter(approved=1)

    return render(request, 'home/all_achievements.html', {'achievements': achievements})
