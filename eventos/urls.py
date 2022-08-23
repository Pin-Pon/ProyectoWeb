from django.urls import path


from . import views



urlpatterns = [
    path('',views.evento, name="EventosNuevos"),
    path('crear/',views.CrearEvento.as_view()),
    path("editar/<int:pk>/", views.Editar.as_view(), name="editar"),
    
]