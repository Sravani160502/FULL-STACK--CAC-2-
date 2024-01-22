from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout

# Create your views here.
def index(request):
    return render(request,"tutor/main/index.html")

def about(request):
    return render(request,"tutor/main/about.html")


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
            return render(request , 'tutor/main/login.html' , {'msg':msg})
    return render(request , 'tutor/main/login.html')


def tutor_register(request):
    return render(request, 'tutor/main/register.html')


        

