from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Transaction, Profile
from django.contrib import messages
from ..forms import ProfileCreationForm
from ..decorators import profile_required


# Create your views here.
@login_required
@profile_required
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
@profile_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'base/user_profile.html', {'profile': profile,'user':request.user})

def profile_create_view(request):
    form = ProfileCreationForm()
    if request.method == 'POST':
        print(request.POST,request.FILES)
        form = ProfileCreationForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Profile was created for {user}')
            return redirect('home')
    context = {'form':form}
    return render(request,'base/profile_create_modal.html',context)



def testing_view(request):
    return render(request,'base/testing.html')