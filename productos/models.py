from django.db import models

# Create your models here.
class Cliente(models.Model):
  nombre = models.CharField(max_length=256)
  apellido = models.CharField(max_length=256)
  dni = models.CharField(max_length=20)
  telefono = models.IntegerField()
  email = models.EmailField()
  fecha_nacimiento = models.DateField()
  
class Producto(models.Model):
  nombre = models.CharField(max_length=256)
  modelo = models.CharField(max_length=256)
  codigo = models.IntegerField()
  disponible = models.BooleanField(default=False)
 
  # Mediante constructor detallo los atributos de instancia mediante variables que el user completa con inputs(no corre inputs)
