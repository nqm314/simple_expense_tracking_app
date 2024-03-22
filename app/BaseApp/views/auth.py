from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from ..forms import SignUpForm
from django.contrib import messages
from ..models import Profile
import logging
logger = logging.getLogger(__name__)

def sign_up_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user}')
            return redirect('sign_in')
    context = {'form':form}
    return render(request,'auth/sign_up.html',context)

def sign_in_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect.')
            return redirect('sign_in')
    context = {'form':form}
    return render(request, 'auth/sign_in.html', context)

def sign_out_view(request):
    logout(request)
    return redirect('sign_in')
