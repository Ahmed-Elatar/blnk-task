from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.models import Group
from ..forms.auth import *
from ..utils import groups


####################################################################################################
#                                      Authentication Views
####################################################################################################

# User Sign-Up
def user_signup(request):
    """
    Handles user registration:
    
    - If the request method is POST, it processes the submitted form.
    - If the form is valid:
        - Sets the user as staff.
        - Assigns the user to a selected role/group.
        - Saves the user and redirects to login.
    - If the request method is GET, displays the signup form.
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.instance.is_staff = True  # Set user as staff
            
            role = form.cleaned_data['role']  # Get the selected role
            print(role)  # Debugging log
            
            user = form.save()  # Save the user instance
            group = Group.objects.get(name=role)  # Fetch the corresponding group
            user.groups.add(group)  # Assign the user to the group

            return redirect('login')  # Redirect to login page

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


# User Login
def user_login(request):
    """
    Handles user authentication and login:
    
    - Redirects authenticated users to the logout page.
    - If the request method is POST:
        - Validates the login form.
        - Authenticates the user with provided credentials.
        - If authentication is successful, logs in the user and redirects to the index page.
    - If the request method is GET, displays the login form.
    """
    if request.user.is_authenticated:
        return redirect('logout')  # Redirect logged-in users to logout

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)  # Log in the user
                return redirect('index')  # Redirect to index page

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


# User Logout
def user_logout(request):
    """
    Logs out the current user and redirects to the login page.
    """
    logout(request)
    return redirect('login')
