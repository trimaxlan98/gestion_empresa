from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('editar/<int:id>/', views.editar_cliente, name='editar_cliente'),  # Nueva ruta
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
]