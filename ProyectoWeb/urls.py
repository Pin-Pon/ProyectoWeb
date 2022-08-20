"""ProyectoWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include , path
from django.contrib.auth import views as auth_views 
from django.conf import settings

#urls general registrar la urls de las apps

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = "login.html") , name= "login" ), 
    path('admin/', admin.site.urls),
    #includes de las apps
    path('eventos/',include('eventos.urls')), 
    path('registro/',include('registro.urls')),
    path('blog/',include('blog.urls')), #registro la app
    path('',include('ProyectoWebApp.urls')),   #registro la app
]
