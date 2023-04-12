from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        rollno = request.POST['rollno']
        studentid = request.POST['studentid']

        user = User.objects.create_user(username=username, password=password)
        user_profile = UserProfile.objects.create(user=user, rollno=rollno, studentid=studentid)

        return redirect('login')

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')

    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('login')

def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    context = {
        'user_profile': user_profile
    }

    return render(request, 'profile.html', context)
