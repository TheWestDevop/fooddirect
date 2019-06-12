from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="index"),
#	path('login',userlogin,name="userlogin"),
#	path('home',userhome,name='userhome'),
#	path('login',userlogin,name="userlogin"),
#	path('logout',userlogout,name="userlogout"),
#	path('auth',userauth,name="userauth"),
#	path('register',userregister,name="userregister"),
#	path('signup',usersignup,name="usersignup")
   
]