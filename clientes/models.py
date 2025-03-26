from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    # Opciones para el campo status
    STATUS_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('pausa', 'En Pausa'),
    ]

    gerente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clientes')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    documento = models.FileField(upload_to='documentos/')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='activo')  # Nuevo campo

    def __str__(self):
        return f"{self.nombre} {self.apellido}"