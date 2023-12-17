from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from .forms import StudentAchievementForm
from users.models import Student
from .models import StudentAchievement
from users.decorators import group_required
from django.urls import reverse_lazy,reverse
from users.views import user_is_faculty
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import JsonResponse


# Create your views here.
def home(request):
    print(request.user)
    print('home')
     # this shows user name in terminal when login is done
    print(request.user.username)
    print(user_is_faculty(request.user))
    return render(request, 'home/home.html', {'title': 'Home'})


@group_required('student')
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
            messages.success(request, f'Your achievement has been submitted for approval!')
            return HttpResponseRedirect(reverse('home:home'))

    else:
        achievement_form = StudentAchievementForm()

    return render(request, 'home/create_achievement.html', { 'form': achievement_form })

@group_required('faculty')
def view_pending(request):
    pending = StudentAchievement.objects.filter(is_pending=1)
    
    return render(request, 'home/pending_achievements.html', {'achievements': pending})

@group_required('faculty', 'student')
def view_details(request, achievement_id):
    achievement = get_object_or_404(StudentAchievement, id=achievement_id)
    if achievement.approved_by == None:
        approved_by = "NOT APPROVED"
    else:
        approved_by = achievement.approved_by.user.first_name + achievement.approved_by.user.last_name

    achievement_type = 'Academic' if achievement.achievement_type == '1' else 'Non-academic'
    details = [
        ('Student Name', achievement.student.user.first_name+ " " + achievement.student.user.last_name ),
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

@group_required( 'student')
def student_view_all(request):
    achievements = get_object_or_404(StudentAchievement,approved=1)

    return render(request, 'home/all_achievements.html', {'achievements': achievements})

@group_required('faculty')
def faculty_view_all(request):
    achievements = StudentAchievement.objects.all()
    return render(request, 'home/all_achievements.html', {'achievements': achievements})

# views.py


@group_required('faculty')
def toggle_approval(request, achievement_id):
    print('toggle_approval')
    achievement = get_object_or_404(StudentAchievement, id=achievement_id)
    print(achievement)
    print(achievement.approved) 
    if request.method == 'POST':
        # Get the approval status from the form submission
        approval_status = request.POST.get('approval_status')
        print(approval_status)

        # Toggle the 'approved' field
        achievement.approved = (approval_status == 'approved')


        # Set the 'approved_by' field if approving
        if achievement.approved:
            achievement.approved_by = request.user.faculty  # Replace with your actual user fetching logic

        achievement.save()

        # Redirect back to the achievement details page after toggling approval
        return redirect('achievement_details', achievement_id=achievement.id)

    # Render the achievement details page when the form is not submitted
    return render(request, "home/achievement_details.html", {'achievement': achievement})
