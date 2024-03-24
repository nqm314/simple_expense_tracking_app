from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    income = MoneyField(max_digits=14, decimal_places=2,default_currency='VND')
    spending_threshold = MoneyField(max_digits=14, decimal_places=2,default_currency='VND')
    profile_picture = models.ImageField(upload_to='profile_pictures')
    def __str__(self) -> str:
        return self.user.__str__()

class TransactionTag(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tags')
    def __str__(self) -> str:
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    amount = MoneyField(max_digits=14, decimal_places=2,default_currency='VND')
    purpose = models.TextField()
    tags = models.ManyToManyField(TransactionTag, related_name='transactions')
    def __str__(self) -> str:
        return f"{self.user.username}'s transaction {self.id}"
