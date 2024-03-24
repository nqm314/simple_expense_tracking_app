from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Transaction, TransactionTag, Profile
from tempus_dominus.widgets import DatePicker

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

class ProfileCreationForm(forms.ModelForm):
    birthdate = forms.DateField(
        widget=DatePicker(
            options={
                'useCurrent': True,
                'collapse': False,
                # Calendar and time widget formatting
                'time': 'fa fa-clock-o',
                'date': 'fa fa-calendar',
                'up': 'fa fa-arrow-up',
                'down': 'fa fa-arrow-down',
                'previous': 'fa fa-chevron-left',
                'next': 'fa fa-chevron-right',
                'today': 'fa fa-calendar-check-o',
                'clear': 'fa fa-delete',
                'close': 'fa fa-times'
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        )
    )
    class Meta:
        model = Profile
        fields = ['phone', 'birthdate', 'income', 'spending_threshold', 'profile_picture']

class TransactionForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=TransactionTag.objects.all(),
        required=False,
    )
    class Meta:
        model = Transaction
        fields = ['amount', 'purpose', 'tags']

class TransactionTagForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=False)
    class Meta:
        model = TransactionTag
        fields = ['name']