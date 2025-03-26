from django.contrib import admin
from django.urls import path, include
from clientes.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('', inicio, name='inicio'),
]