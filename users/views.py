from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import StudentRegistrationForm, CustomUserForm, FacultyRegistrationForm
from .models import CustomUser, Student
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import StudentLoginForm, FacultyLoginForm
# messages
from django.contrib import messages
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
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                # Redirect to student dashboard or any other page
                return HttpResponseRedirect(reverse("users:registration_success")) # sending to same registration success page for example
    else:
        form = StudentLoginForm()

    return render(request, 'users/student_login.html', {'stu_login_form': form})

def faculty_login(request):
    if request.method == 'POST':
        form = FacultyLoginForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, **form.cleaned_data)
            if user is not None:
                login(request, user)
                # Redirect to faculty dashboard or any other page
                return HttpResponseRedirect(reverse("users:registration_success")) # sending to same registration success page for example
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

