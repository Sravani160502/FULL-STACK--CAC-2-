from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout


def index(request):
    return render(request,"learner/main/index.html")

def about(request):
    return render(request,"learner/main/about.html")

def courses(request):
    return render(request,"learner/main/courses.html")
# Create your views here.


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username , password=password)
        if user is not None and user.is_active:
            if user.is_superuser==False and user.is_staff==False:
                login(request,user)
                return redirect('index')
        elif user is None:
            msg = "Wrong credentials. Please try again!"
            return render(request , 'learner/main/login.html' , {'msg':msg})
    return render(request , 'learner/main/login.html')
