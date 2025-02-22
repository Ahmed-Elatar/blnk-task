from django.shortcuts import render

from ..utils import groups

from django.shortcuts import render,redirect,get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout,get_user
from django.contrib.auth.models import Group
from ..forms.auth import *
# Create your views here.












####################################################################################################
##################                  Authentication

#sign-up 
def user_signup(request):
  
    if request.method == 'POST':
        form = SignupForm(request.POST)
  
        if form.is_valid():
            form.instance.is_staff = True
            
            role =form.cleaned_data['role']
            print(role)
            
            user = form.save()
            group = Group.objects.get(name=role)
            user.groups.add(group)


            return redirect('login')
  
    else:
        form = SignupForm()
  
    return render(request, 'signup.html', {'form': form})



# login
def user_login(request):

    if request.user.is_authenticated:
        return redirect ('logout')
  
    if request.method == 'POST':
        

        form = LoginForm(request.POST)
    
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
    
            if user:
                login(request, user)    
                return redirect('index')
    
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


# logout page
def user_logout(request):
    
    logout(request)
    return redirect('login')