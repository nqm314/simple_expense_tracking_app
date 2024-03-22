from django.urls import path
from . import views
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('transactions/', views.transactions_view, name='transactions'),
    path('add_transaction/', views.add_transaction_view, name='add_transaction'),
    path('auth/sign_up/', views.sign_up_view, name='sign_up'),
    path('auth/sign_in/', views.sign_in_view, name='sign_in'),
    path('auth/sign_out/', views.sign_out_view, name='sign_out'),
    path('profile/view/', views.profile_view, name='profile'),
    path('testing/', views.testing_view, name='testing'),
    path('profile/create/',views.profile_create_view, name='create_profile')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)