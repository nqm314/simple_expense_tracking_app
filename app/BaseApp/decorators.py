from django.shortcuts import redirect
from django.contrib import messages
from .models import Profile

def profile_required(function):
    def wrap(request, *args, **kwargs):
        try:
            Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            messages.info(request, 'Profile not created')
            return redirect('create_profile')  # Redirect to profile creation
        return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
