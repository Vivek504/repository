from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid username or password')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Please try with other username')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email)
                user.save();   
                return redirect('/login')
        else:
            messages.info(request,'Please enter the same password')
            return redirect('register')
    else:
        return render(request,'register.html')