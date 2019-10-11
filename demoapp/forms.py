from django import forms
from django.forms import ModelForm
from .models import Employee, UserProfileInfo,Reg
from django.contrib.auth.models import User

class EmpForm(forms.ModelForm):
     fname= forms.CharField()
     email= forms.EmailField()
     age =forms.IntegerField()

     class Meta:
         model = Employee
         fields= '__all__'


#***********************************************************************************#


class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model= User
        fields= ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model= UserProfileInfo
        fields= ['profile_pic','profile_url']


#************************************************************

class RegForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())
    username=forms.CharField()
    email= forms.EmailField()


    class Meta:
        model= User
        fields=['username', 'email', 'password']
