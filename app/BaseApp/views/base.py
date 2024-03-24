from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import Transaction, Profile, TransactionTag
from django.contrib import messages
from ..forms import ProfileCreationForm, TransactionForm, TransactionTagForm
from ..decorators import profile_required
from django.shortcuts import get_object_or_404

def transaction_detail(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    return render(request, 'base/transaction_detail.html', {'transaction': transaction})


# Create your views here.
@login_required
@profile_required
def home(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'base/home.html', {'transactions': transactions})


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

@login_required
def create_transaction_view(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        tag_form = TransactionTagForm(request.POST)
        if form.is_valid() and tag_form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            tag = tag_form.save(commit=False)
            tag.user = request.user
            tag.save()
            transaction.tags.add(tag)
            return redirect('home')
    else:
        form = TransactionForm()
        tag_form = TransactionTagForm()
    return render(request, 'base/create_transaction.html', {'form': form, 'tag_form': tag_form})

def testing_view(request):
    return render(request,'base/testing.html')