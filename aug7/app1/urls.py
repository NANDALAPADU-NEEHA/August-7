from django.urls import path
from app1 import views

urlpatterns=[
    path('',views.home,name='homepage'),
    path('login',views.loginv,name='loginpage'),
    path('register',views.register,name='registerpage'),
    path('create',views.create,name='createpage'),
    path('profile',views.profile,name='profilepage'),
    path('logout',views.logoutv,name='logoutpage'),
    
]
