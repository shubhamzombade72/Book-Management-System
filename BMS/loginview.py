from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages  # To send feedback messages
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def Signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=pass1)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('/login/')
        else:
            messages.error(request, 'Passwords do not match')

    return render(request, "logins/signup.html")


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        pass1 = request.POST.get('pass1')  
        
        
        user = authenticate(request, username=username, password=pass1)
        
        if user is not None:
            login(request, user) 
            messages.success(request, 'Login successful')  
            return redirect('/dashboard/')  
        else:
            messages.error(request, 'Invalid username or password') 

    return render(request, "logins/login.html")

