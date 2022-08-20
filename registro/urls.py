from django.urls import path
from django.contrib.auth import views as auth_views


from .views import Registro 


urlpatterns = [
    
    
    path('',Registro.as_view(), name="Registro"),     
]

#vista basada en clcs para el login
 #   path('login/', auth_views.LoginView.as_view(template_name = "login.html") , name= "login" )




