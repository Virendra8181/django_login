from email import message
from pyexpat.errors import messages
from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def handelsignup(request):
    if request.method == "POST":
        username=request.POST['Username']
        gmail=request.POST['Email']
        password=request.POST['Password']
        myuser=User.objects.create_user(username,gmail,password)
        myuser.save()
        messages.success(request,"your accont is success signup")
        return render(request,"index.html")
    else:
        return HttpResponse("404 - not found")


def home(request):
    messages.success(request,"your accont is success signup")
    return render(request,"homepage.html")


def loginpage(request):
    if request.method=="POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
          
            messages.success(request,"success fully login page ")
           
            return redirect('/home')
        else:
            messages.error(request,"please enter your right id and password")
    return  render(request,"index1.html")

def signuppage(request):
    return render(request,"index1.html")

