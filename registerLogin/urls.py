from django.urls import path
from registerLogin.views import show_registerlogin
from registerLogin.views import register 
from registerLogin.views import login_user 


app_name = 'registerLogin'

urlpatterns = [
    path('', show_registerlogin, name='show_registerlogin'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'), 
]