from django.db import models

# Create your models here.

# Estoy creando la clase Curso, que hereda la clase Model. 
class Curso(models.Model):
    nombre = models.CharField(max_length = 40)
    camada = models.IntegerField()
    
class Alumno(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20) 
    legajo = models.IntegerField()
    
class Profesor(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20) 
    curso = models.CharField(max_length = 40) 


