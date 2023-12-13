from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import StudentRegistrationForm, CustomUserForm, FacultyRegistrationForm
from .models import CustomUser, Student

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
    if request.method == 'POST':
        print('stu works')
        user_form = CustomUserForm(request.POST)
        student_form = StudentRegistrationForm(request.POST)
        print('stu works')
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            print('stu works')
            # Create a Student instance associated with the user
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            print('stu works')

            return redirect('registration success')  # Redirect to the home page or a specific URL after registration
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

            # Redirect to a success page or any other page you prefer
            return redirect('registration_success')  

    else:
        user_form = CustomUserForm()
        faculty_form = FacultyRegistrationForm()

    return render(request, 'faculty_registration.html', {'user_form': user_form, 'faculty_form': faculty_form,'user_type':'Faculty'})

def registration_success(request):
    return render(request, 'users/registration_success.html') 