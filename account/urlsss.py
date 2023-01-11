from django.urls import path 
from . import views

urlpatterns = [
    path('login_request',views.login_request,name='login_request'),
    path('change_password',views.change_password,name='change_password'),
    path('logout_request',views.logout_request,name='logout_request'),
    path("profile",views.profile,name="profile"),
   

    
]