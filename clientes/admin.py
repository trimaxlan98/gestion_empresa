from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'get_status_display')  # Mostrar estado
    list_filter = ('status',)  # Filtrar por estado
    search_fields = ('nombre', 'apellido', 'email')  # Buscar por nombre, apellido o email