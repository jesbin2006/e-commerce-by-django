from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout
from . models import customer
from django.contrib import messages
def sign_out(request):
    logout(request)
    return redirect('home')
# Create your views here.
def account(request):
    try:
        if request.POST and 'register' in request.POST: 
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            phone=request.POST.get('phone')
        #create user account
            user=User.objects.create_user(
               username=username,
               password=password,
               email=email
            )
        #create customer account
            Customer=customer.objects.create(
               name=username, 
               user=user,
               phone=phone
            )
            return redirect('home')
    except Exception as e:
        error_message="same username or invalid fillings "
        messages.error(request,error_message)
     
    if request.POST and 'login'in  request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid user')

    return render(request,'account.html')