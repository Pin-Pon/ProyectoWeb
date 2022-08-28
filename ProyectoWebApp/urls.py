from django.urls import path
from  django.contrib.auth import views as auth_views
#from .views import login_view 
from ProyectoWebApp import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
app_name = 'ProyectoWebApp'

urlpatterns = [
   
    path('',views.inicio, name="Inicio"),
     #path('login/',login_view, name="login"),
    # path('logout/',auth_views.LogoutView.as_view(template_name="ProyectoWebApp/inicio.html"), name="logout"),
    
    
   
    path('calendario/',views.calendario, name="Calendario"),
    path('contacto',views.contacto, name="Contacto"),
    path("asistir/<int:id_usuario>/<int:id_evento>", views.Asistir, name = "asistir"),
    path("eliminarasistencia/<int:id_usuario>/<int:id_evento>", views.EliminarAsistencia, name = "EliminarAsistencia"),      
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) #mostrar la foto en el servidor





