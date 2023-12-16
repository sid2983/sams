from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect

from django.shortcuts import reverse
from functools import wraps
from django.contrib.auth.decorators import login_required
from users.views import user_is_student, user_is_faculty
from django.contrib import messages

# def group_required(*group_names, login_url=None):
#     """Requires user membership in at least one of the groups passed in."""
#     def in_group(user):
#         if user.groups.filter(name__in=group_names).exists() or user.is_superuser:
#             return True
#         return False

#     return user_passes_test(in_group, login_url=login_url)

def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""
    def in_group(user):
        if user.groups.filter(name__in=group_names).exists() or user.is_superuser:
            return True
        return False

    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            if in_group(request.user):
                return view_func(request, *args, **kwargs)
            else:
                # Redirect to different login URLs based on user type
                if user_is_student(request.user):
                    login_url = reverse('users:student_login')
                    message = "You need to be a student to access this page."
                elif user_is_faculty(request.user):
                    login_url = reverse('users:faculty_login')
                    message = "You need to be a faculty member to access this page."
                else:
                    login_url = '/accounts/login/'  # Default login URL
                    message = "You need to be logged in to access this page."

                messages.error(request, message)
                return redirect(login_url)

        return wrapped_view

    return decorator



# def login_required_with_type(login_url, user_type):
#     def decorator(view_func):
#         @wraps(view_func)
#         def wrapped_view(request, *args, **kwargs):
#             # Check the user type and set the appropriate login URL
#             if user_type == 'student':
#                 actual_login_url = reverse('users:student_login')
#             elif user_type == 'faculty':
#                 actual_login_url = reverse('users:faculty_login')
#             else:
#                 raise ValueError("Invalid user type")

#             return login_required(login_url=actual_login_url)(view_func)(request, *args, **kwargs)

#         return wrapped_view

#     return decorator
