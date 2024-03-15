from django.contrib import admin
from .models import Profile, TransactionTag, Transaction

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',  'phone',)  # Customize this list as needed

admin.site.register(TransactionTag)
admin.site.register(Transaction)
admin.site.register(Profile, ProfileAdmin)