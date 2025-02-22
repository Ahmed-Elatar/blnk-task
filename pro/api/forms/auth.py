from django import forms 

from ..models.provider import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User







UserRole =( 
    ("Bank_personal", "Bank_personal"), 
    ("Loan_Provider", "Loan_Provider"),
    ("Loan_Customer", "Loan_Customer"), 
     
    
) 

class SignupForm(UserCreationForm):
    role = forms.ChoiceField(choices = UserRole) 
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2','role']
        


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User 
        fields = ['username', 'password']
