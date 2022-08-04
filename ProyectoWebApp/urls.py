from django.urls import path

from ProyectoWebApp import views

urlpatterns = [
   
    path('',views.inicio, name="Inicio"),
    path('login',views.login, name="Login"),
    path('eventos',views.eventos, name="Eventos"),
    path('calendario',views.calendario, name="Calendario"),
    path('blog',views.blog, name="Blog"),
    path('contacto',views.contacto, name="Contacto"), 
      
]





