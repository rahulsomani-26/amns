from django import forms 

# Registration Form 

# class RegistrationForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User 
        fields = ['username','email','password1','password2']

