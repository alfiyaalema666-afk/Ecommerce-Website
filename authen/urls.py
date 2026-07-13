from django.urls import path
from .views import *

urlpatterns = [
    path('register/',register,name='register'),
    path('login_/',login_,name='login_'),
    path('profile/',profile,name='profile'),
    path('logout_/',logout_,name='logout_'),
    path('forgot_password/',forgot_password,name='forgot_password'),
    path('reset/',reset_pass,name='reset_pass'),
    path('update/',update,name='update'),

]