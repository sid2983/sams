from django.shortcuts import render
#import current_user


# Create your views here.
def home(request):
    print(request.user) # this shows user name in terminal when login is done
    return render(request, 'home/home.html', {'title': 'Home'})