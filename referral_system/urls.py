from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('register/', register_user, name='register'),
    path('user-details/', user_details, name='user-details'),
    path('user-referrals/', user_referrals, name='user-referrals'),
]
