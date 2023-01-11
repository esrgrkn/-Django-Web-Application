
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .forms import LoginUserForm,NewUserForm,UserForm,ProfileForm 
from django.contrib.auth.models import User  
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
import time

# Create your views here.


def login_request(request):
   if request.user.is_authenticated:
    return redirect("home") 

   if request.method == "POST":
        form=LoginUserForm(request,data=request.POST) 
        
        if form.is_valid():                           
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
        
            user=authenticate(request,username=username,password=password) 

            if user is not None:                      
                login(request,user)
                return redirect("home")
            else:
                return render(request, 'accountapp/login.html', {'form':form})
        else:
                return render(request, 'accountapp/login.html', {'form':form})

   else:
        form = LoginUserForm()
        return render(request, 'accountapp/login.html', {'form':form})



def profile(request):
    
    return render(request,"accountApp/profile.html")


def change_password(request):

    if request.method == 'POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"password change successful")
            return render(request,"accountApp/anasayfa.html")
        else:
            return render(request,"accountApp/changePassword.html",{"form":form})
    else:    
        form=PasswordChangeForm(request.user)
        return render(request,"accountApp/changePassword.html",{"form":form})



   



def logout_request(request):
     logout(request)
     return redirect("login_request")