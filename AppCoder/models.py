from django.db import models

# Create your models here.

# Estoy creando la clase Curso, que hereda la clase Model. 
class Curso(models.Model):
    nombre = models.CharField(max_length = 40)
    camada = models.IntegerField()
    
class Alumno(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20) 
    email = models.EmailField(max_length = 30 , default='default_value')
    contraseña = models.CharField(max_length=255, default='default_value') 
    
class Profesor(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20) 
    curso = models.CharField(max_length = 40) 


