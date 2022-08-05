from django.urls import path

from ProyectoWebApp import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
   
    path('',views.inicio, name="Inicio"),
    path('login',views.login, name="Login"),
    path('evento',views.evento, name="Eventos"),
    path('calendario',views.calendario, name="Calendario"),
    path('blog',views.blog, name="Blog"),
    path('contacto',views.contacto, name="Contacto"),      
]
urlpatterns += staticfiles_urlpatterns()





