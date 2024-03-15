from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Transaction, Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'base/home.html')


@login_required
def transactions_view(request):
    profile = Profile.objects.get(user=request.user)
    transactions = Transaction.objects.filter(profile=profile)
    return render(request, 'transactions.html', {'transactions': transactions})

@login_required
def add_transaction_view(request):
    # Add your code here to handle the form submission
    pass

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
    return render(request,'user/sign_up.html',context)

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
    return render(request, 'user/sign_in.html', context)

def sign_out_view(request):
    return redirect('sign_in')

def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'base/user_profile.html', {'profile': profile,'user':request.user})

def testing_view(request):
    return render(request,'user/testing.html')