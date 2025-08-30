from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST.get('role', 'user')  # role select karega

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)

        # Simple Role System
        if role == "admin":
            user.is_staff = True
        else:
            user.is_staff = False
        user.save()

        messages.success(request, "Account created successfully!")
        return redirect('login')
    return render(request, 'register.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')

