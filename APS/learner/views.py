from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout


def index(request):
    return render(request,"learner/main/index.html")

def about(request):
    return render(request,"learner/main/about.html")

def courses(request):
    return render(request,"learner/main/courses.html")

# def register(request):
#     return render(request,"learner/main/register.html")
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

def register(request):
    errors={}
    if request.method=="POST":
        username=request.POST['username'].strip()
        name=request.POST['name'].strip()
        password=request.POST['password'].strip()
        phone=request.POST['phone'].strip()
        qualification=request.POST['qualification'].strip()
        interests=request.POST['interests'].strip()
        improvements=request.POST['improvements'].strip()
        if not username:
            errors['username']="Username Field is Required"
        else:
            is_used=User.objects.filter(username=username).exists()
            if is_used:
                errors['username']="Username is already taken"
        
        if not password:
            errors['password']="Password is required"
        
        is_valid=len(errors.keys())==0
        if is_valid:
            user=User.objects.create_user(
                username=username,
                name=name,
                password=password,
                phone=phone,
                qualification=qualification,
            )
            user=authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/?signup=successful')
            
    context={
            'errors':errors
        }
    return render(request,'register.html')