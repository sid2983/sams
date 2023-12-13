# # forms for registration  of users
# ## student

# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser,Student,Faculty

# class CustomUserSignUpForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser

# class StudentSignUpForm(CustomUserSignUpForm):
#     # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     # enrollment_number = forms.CharField(max_length=20)
#     # batch_year = forms.IntegerField()
#     # semester = forms.IntegerField()
#     # section = forms.CharField(max_length=10)
#     # shift = forms.CharField(max_length=10)
#     class Meta:
#         model = Student
#         fields = ('username', 'email', 'password1', 'password2','enrollment_number','batch_year','semester','section','shift')

# class FacultySignUpForm(CustomUserSignUpForm):
#     # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#     # enrollment_number = forms.CharField(max_length=20)
#     # batch_year = forms.IntegerField()
#     # semester = forms.IntegerField()
#     # section = forms.CharField(max_length=10)
#     # shift = forms.CharField(max_length=10)
#     class Meta:
#         model = Faculty
#         fields = ('username', 'email', 'password1', 'password2', 'employee_id', 'shift', 'designation')

# users/forms.py
# users/forms.py

from django import forms

from .models import CustomUser, Student, Faculty

class CustomUserForm(forms.ModelForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2', 'profile_picture', 'portfolio_links', 'department']
        labels = {
            'profile_picture': 'Profile Picture',
            'portfolio_links': 'Portfolio Links',
            'department': 'Department',
            'password2': 'Confirm Password',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }
        required = {
            'username': 'True',
            'email': 'True',
            'first_name': 'True',
            'last_name': 'True',

        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError(
                "Passwords do not match"
            )

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['enrollment_number', 'batch_year', 'semester', 'section', 'shift']
        labels = {
            'enrollment_number': 'Enrollment Number',
            'batch_year': 'Batch Year',
            'semester': 'Semester',
            'section': 'Section',
            'shift': 'Shift',
        }

class FacultyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['employee_id', 'shift', 'designation']
        labels = {
            'employee_id': 'Employee ID',
            'shift': 'Shift',
            'designation': 'Designation',
        }