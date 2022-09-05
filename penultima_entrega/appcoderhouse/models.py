from pyexpat import model
from django.db import models

# Create your models here.
class Alumno(models.Model):
    #El id se crea automático.
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    #Para llevar un log de la creación / modificaciones del registro
    last_update = models.DateTimeField(auto_now=True)
    add_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.apellido}, {self.nombre}';

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    #Acepta nulls (null=True), también podría ser para los formularios blank=True para no obligar a rellenar el campo.
    profesion = models.CharField(max_length=50,null=True)
    email = models.EmailField()
    last_update = models.DateTimeField(auto_now=True)
    add_date = models.DateTimeField(auto_now_add=True)
    def __srt__(self):
        return f'{self.apellido}, {self.nombre}'

class Curso(models.Model):
    camada = models.IntegerField(default=0)
    nombre = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    last_update = models.DateTimeField(auto_now=True)
    add_date = models.DateTimeField(auto_now_add=True)
    class Meta: 
        ordering = ['-last_update']
    def __str__(self):
        return self.nombre
'''
class Entrega(model.Models):
    titulo = models.CharField(max_length=100)
    desc = models.CharField(max_length= 100)
    fecha_desde = models.DateTimeField()
    fecha_hasta = models.DateTimeField()
    entregado = models.BooleanField()
'''
    
