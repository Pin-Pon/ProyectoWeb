from django.urls import path

from . import views

# app_name='eventos'

urlpatterns = [
    path('',views.evento, name="Eventos"),
    path('crear/',views.CrearEvento.as_view()),
    
]