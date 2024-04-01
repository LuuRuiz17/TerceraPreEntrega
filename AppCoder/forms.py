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
    legajo = forms.IntegerField()
    
