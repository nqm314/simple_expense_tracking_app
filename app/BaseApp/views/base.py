from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Transaction, Profile
from django.contrib import messages


# Create your views here.
@login_required
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

@login_required
def profile_view(request):
    try: 
        profile = Profile.objects.get(user=request.user)
        return render(request, 'base/user_profile.html', {'profile': profile,'user':request.user})
    except Profile.DoesNotExist:
        messages.info(request, 'Profile not created')
        return redirect('testing') # should redirect to a create 

def testing_view(request):
    return render(request,'user/testing.html')