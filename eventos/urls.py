from django.urls import path


from . import views



urlpatterns = [
    path('',views.evento, name="EventosNuevos"),
    path('crear/',views.CrearEvento.as_view(),name="CrearEvento"),
    path("editar/<int:pk>/", views.Editar.as_view(), name="editar"),
    path("eliminar/<int:pk>/", views.Eliminar.as_view(), name="Eliminar"),
    
]