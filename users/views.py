from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistrationForm, CustomUserForm, FacultyRegistrationForm
from .models import CustomUser, Student, Faculty
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import StudentLoginForm, FacultyLoginForm
# messages
from django.contrib import messages
# groups
from django.contrib.auth.models import Group

# Create your views here.
# def studentRegistration(request):
#     if (request.method == 'POST'):
#         forms.StudentRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("success"))

#     else:
#         form =forms.StudentSignUpForm()

#     return render()
        
            
# users/views.py



def student_registration(request):
    print('not works')
    if request.method == 'POST':
        print('stu works')
        user_form = CustomUserForm(request.POST)
        student_form = StudentRegistrationForm(request.POST)
        print('stu works')
        if user_form.is_valid() and student_form.is_valid() and user_form.data != None and student_form.data != None:
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            print('stu works')

             # Assign the user to the 'student' group
            student_group = Group.objects.get(name='student')
            user.groups.add(student_group)

            # Create a Student instance associated with the user
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            print('stu works')
            print(user_form.data,student_form.data)
            return HttpResponseRedirect(reverse("users:registration_success"))  
        # Redirect to the home page or a specific URL after registration
        else:
            print("No data Sent")
    else:
        user_form = CustomUserForm()
        student_form = StudentRegistrationForm()

    return render(request, 'users/student_registration.html', {'user_form': user_form, 'student_form': student_form,'usertype':'Student'})




def faculty_registration(request):
    if request.method == 'POST':
        print('fac works')
        user_form = CustomUserForm(request.POST)
        faculty_form = FacultyRegistrationForm(request.POST)

        if user_form.is_valid() and faculty_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Assign the user to the 'faculty' group
            faculty_group = Group.objects.get(name='faculty')
            user.groups.add(faculty_group)

            faculty = faculty_form.save(commit=False)
            faculty.user = user
            faculty.save()
            print('fac works')
            # Redirect to a success page or any other page you prefer
            return HttpResponseRedirect(reverse("users:registration_success")) # sending to same registration success page for example

    else:
        user_form = CustomUserForm()
        faculty_form = FacultyRegistrationForm()

    return render(request, 'users/faculty_registration.html', {'user_form': user_form, 'faculty_form': faculty_form,'user_type':'Faculty'})

def registration_success(request):
    return render(request, 'users/registration_success.html') 


# users/views.py



def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None and user.groups.filter(name='student').exists():
                login(request, user)
                messages.success(request, 'Login successful.')
                return HttpResponseRedirect(reverse("home:home"))  # Redirect to student dashboard or home page
            else:
                messages.error(request, 'Invalid login credentials or you do not have access.')
    else:
        form = StudentLoginForm()

    return render(request, 'users/student_login.html', {'stu_login_form': form})

def faculty_login(request):
    if request.method == 'POST':
        form = FacultyLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None and user.groups.filter(name='faculty').exists():
                login(request, user)
                messages.success(request, 'Login successful.')
                return HttpResponseRedirect(reverse("home:home"))  # Redirect to faculty dashboard or home page
            else:
                messages.error(request, 'Invalid login credentials or you do not have access.')
    else:
        form = FacultyLoginForm()

    return render(request, 'users/faculty_login.html', {'fac_login_form': form})



#faculty_logout
def faculty_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return HttpResponseRedirect(reverse("home:home")) 

#student_logout
def student_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return HttpResponseRedirect(reverse("home:home"))

def user_is_faculty(user):
    try:
        return hasattr(user, 'faculty')
    except Faculty.DoesNotExist:
        return False
    
def user_is_student(user):
    try:
        return hasattr(user, 'student')
    except Student.DoesNotExist:
<<<<<<< HEAD
        return False
@login_required(login_url="/users/studentLogin/")
def dashboard_view(request):
    username = request.user.get_full_name()

    return render(request, 'users/dashboard.html', {'user_name': username})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return HttpResponseRedirect(reverse("home:home"))
=======
        return False
>>>>>>> c3af2fe (Dashboard code)
