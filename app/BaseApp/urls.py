from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('transactions/', views.transactions_view, name='transactions'),
    path('add_transaction/', views.add_transaction_view, name='add_transaction'),
    path('sign_up/', views.sign_up_view, name='sign_up'),
    path('sign_in/', views.sign_in_view, name='sign_in'),
    path('sign_out/', views.sign_out_view, name='sign_out'),
    path('profile/', views.profile_view, name='profile'),
    path('testing/', views.testing_view, name='testing'),
]