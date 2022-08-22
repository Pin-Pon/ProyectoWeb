from django.urls import path
from  django.contrib.auth import views as auth_views
from .views import login_view 
from ProyectoWebApp import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
   
    path('',views.inicio, name="Inicio"),
    path('login/',login_view, name="login"),
    
    
   
    path('calendario',views.calendario, name="Calendario"),
    path('contacto',views.contacto, name="Contacto"),      
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #mostrar la foto en el servidor





