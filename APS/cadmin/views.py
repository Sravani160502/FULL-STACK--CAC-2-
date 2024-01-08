from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout


def dashboard(request):
    return render(request , 'admin/main/dasboard.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username , password=password)
        if user is not None and user.is_superuser==True :
            login(request , user)
            return render(request , 'admin/main/dashboard.html')
        elif user is None:
            msg = "Wrong credentials. Please try again!"
            return render(request , 'admin/main/login.html' , {'msg':msg})
    return render(request , 'admin/main/login.html')
