from django.db import models

# Create your models here.

# Estoy creando la clase Curso, que hereda la clase Model. 
class Curso(models.Model):
    nombre = models.CharField(max_length = 40)
    camada = models.IntegerField()
    
    def __str__(self):
        return f"Curso: {self.nombre} - Comisión: {self.camada}"
    
class Alumno(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20) 
    email = models.EmailField(max_length = 30 , default='default_value')
    contraseña = models.CharField(max_length=255, default='default_value') 
    
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido} - Email: {self.email} "
    
class Profesor(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20) 
    curso = models.CharField(max_length = 40) 
    
    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido} - Curso: {self.curso}"


