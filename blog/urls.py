from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
   
    path('',views.blog.as_view(), name="Blog"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
    path('crearpost/', views.CrearPost.as_view(), name="CrearPost"),
        
]