from django import forms

class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    
class Profesor_formulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length = 20) 
    curso = forms.CharField(max_length = 40) 
    
class Alumno_formulario(forms.Form):
    nombre = forms.CharField(max_length = 20)
    apellido = forms.CharField(max_length = 20) 
    email = forms.EmailField(max_length = 50)
    contraseña = forms.CharField(max_length = 30)
    
