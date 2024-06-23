
from django.contrib import admin
from django.urls import path
from aalu import views


urlpatterns = [
   path('',views.index,name='aalu'),
  

   path("login.html",views.login,name='aalu'),
   path("signin.html",views.signin,name='signin'), 
   path("review1.html",views.review1,name='aalu'),
   path("userRev.html",views.userRev,name='aalu'),
  
]


