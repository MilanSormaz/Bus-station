from django.urls import path
from . views import register
from . import views
from django.contrib.auth import views as authentication_views


app_name = 'users'

urlpatterns = [    
    path('register/', register, name='register'),
  
]