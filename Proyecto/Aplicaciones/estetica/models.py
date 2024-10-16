from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Turno(models.Model):
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Relación con el modelo Usuario
    servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)  # Relación con Servicio
    fecha_hora = models.DateTimeField()  # Fecha y hora del turno
    estado = models.CharField(max_length=20, choices=[
        ('reservado', 'Reservado'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
    ], default='reservado')  # Estado del turno
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del servicio
    senal_pagada = models.BooleanField(default=False)  # Indica si se ha pagado una seña
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Monto total pagado
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación del turno
    cambio_permitido = models.IntegerField(default=1)  # Número de cambios de turno permitidos

    def __str__(self):
        return f'Turno: {self.fecha_hora} - Cliente: {self.cliente.username}'


class Servicio(models.Model):
    nombre = models.CharField(max_length=255)  # Nombre del servicio
    descripcion = models.TextField(blank=True, null=True)  # Descripción del servicio
    duracion = models.IntegerField()  # Duración del servicio en minutos
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del servicio

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)  # Nombre del producto
    descripcion = models.TextField(blank=True, null=True)  # Descripción breve del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio del producto
    stock = models.IntegerField(default=0)  # Cantidad disponible en inventario
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  # Imagen del producto

    def __str__(self):
        return self.nombre
