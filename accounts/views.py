from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,('login successfull!'))
            return redirect('home')
        else:
            messages.success(request,('login failed!'))
            return redirect('login') 

    else:
        return render(request,'login.html')

def user_logout(request):
    logout(request) 
    messages.success(request,('logout successfull!'))
    return redirect('dashboard_home')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        company = request.POST['company']
        role = request.POST['role']

        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()

        profile = Profile.objects.create(user_account=user,company=company,role=role)
        profile.save()
        return redirect('home')
    else:
        return render(request,'register.html')