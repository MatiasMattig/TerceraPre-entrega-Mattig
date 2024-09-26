from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_reserva, name='registrar_reserva'),
    path('reservas/', views.lista_reservas, name='reserva_lista'),
    path('buscar/', views.buscar_reservas, name='buscar_reservas'),
]
