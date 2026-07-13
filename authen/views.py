from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def register(request):
    if request.method == 'POST':
          try:
            u = User.objects.get(username=request.POST['username'])
            return render(request,'register.html',{'error':'Username already exists'})
          except:
               u = User.objects.create(
                    first_name = request.POST['fname'],
                    last_name = request.POST['lname'],
                    email = request.POST['email'],
                    username = request.POST['username']
               )
               profile = Profile.objects.create(
                user=u,
                phone=request.POST['phone'],
                address=request.POST['address']
            )
               u.set_password(request.POST['password'])
               u.save()
               profile.save()
               print(request.POST)
               print(request.POST.get("phone"))
               print(request.POST.get("address"))
               return redirect('login_')
    return render(request,'register.html')

def login_(request):
    if request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        u = authenticate(username=request.POST['username'],password=request.POST['password'])#user object instance #None
        if u:#user obj instance ---> True #None ---> False
            login(request,u)
            return redirect('home')
        else:
            return render(request,'login_.html',{'error':'Invalid username or password'})
    return render(request,'login_.html')

def profile(request):
    return render(request,'profile.html')

def logout_(request):
    logout(request)
    return redirect('login_')

def forgot_password(request):
    return render(request,'forgot_password.html')

@login_required(login_url='login_')
def reset_pass(request):
    if request.method == 'POST': 
        if 'new_pass' in request.POST:
            u = User.objects.get(username=request.user.username)
            new=request.POST['new_pass']
            confirm=request.POST['confirm_pass']
            if new == confirm:
                u.set_password(request.POST['new_pass'])
                u.save()
                return redirect('login_')
            else:
                return render(request,'reset_pass.html',{'error':'Passwords do not match'})
    return render(request,'reset_pass.html')

def update(request):
    if request.method == 'POST':
        u = User.objects.get(username=request.user.username)
        profile, created = Profile.objects.get_or_create(
            user=u,
            defaults={
                "phone": "",
                "address": ""
            }
            )
        u.first_name = request.POST['fname']
        u.last_name = request.POST['lname']
        u.email = request.POST['email']
        profile.phone = request.POST['phone']
        profile.address = request.POST['address']
        u.save()
        profile.save()
        print(u.first_name,u.last_name,u.email)
        return redirect('profile')
    return render(request,'update.html')
