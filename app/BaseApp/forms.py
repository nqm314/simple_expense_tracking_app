from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Transaction, TransactionTag, Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="First name", widget=forms.TextInput(attrs={'placeholder': ''}))
    last_name = forms.CharField(label="Last name", widget=forms.TextInput(attrs={'placeholder': ''}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ''}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': ''}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': ''}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': ''}))
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields ='__all__'
