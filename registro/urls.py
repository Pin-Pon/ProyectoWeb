from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


from .views import Registro 
#  login_view

urlpatterns = [
    
    
    path('',views.Registro.as_view(), name="Registro"), 
    # path('login/',login_view, name="login"),
    
 
]

#vista basada en clcs para el login
 #   path('login/', auth_views.LoginView.as_view(template_name = "login.html") , name= "login" )




