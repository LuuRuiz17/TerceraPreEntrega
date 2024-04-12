from django.shortcuts import render
from django.shortcuts import redirect
from AppCoder.models import Curso
from AppCoder.models import Alumno
from AppCoder.models import Profesor
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario
from .forms import Profesor_formulario
from .forms import Alumno_formulario


# Create your views here.

# model Alumno

def login(request):
    return render(request , "login.html")

def alta_alumno(request , nombre , apellido , email , contraseña):
    alumno = Alumno(nombre = nombre.title() , apellido = apellido.title() , email = email , contraseña = contraseña)
    alumno.save()
    texto = f"Se guardó en la Base de Datos el Alumno: {alumno.nombre} {alumno.apellido}"
    return HttpResponse(texto)


def ver_alumnos(request):
    alumnos = Alumno.objects.all()
    diccionario = {"alumnos" : alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)


def alumno_formulario(request):
    
    if request.method == "POST":
        
        mi_formulario = Alumno_formulario(request.POST)
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno(nombre = datos["nombre"].title() , apellido = datos["apellido"].title() , email = datos["email"] , contraseña = datos["contraseña"])
            alumno.save()
            
            return render(request , "form_alumno.html")
            
    return render(request , "form_alumno.html") 
    
def inicio(request):
    return render(request , "inicio.html")  
    
def alta_curso(request, nombre , camada):
    curso = Curso(nombre = nombre.title() , camada = camada)
    curso.save()
    texto = f"Se guardó en la Base de Datos el Curso {curso.nombre} {curso.camada}"
    return HttpResponse(texto)

def ver_cursos(request):
    cursos = Curso.objects.all()
    # cantidad_cursos = len(cursos)
    diccionario = {"cursos" : cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
    # return HttpResponse(cantidad_cursos)

def curso_formulario(request):
    
    if request.method == "POST":
        
        mi_formulario = Curso_formulario(request.POST)
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso = Curso(nombre = datos["nombre"].title() , camada = datos["camada"])
            curso.save()
            
            return render(request , "formulario.html")
            
    return render(request , "formulario.html") 

# Las peticiones son de tipo get por default.
# La petición get pide datos, mientras que post envía datos al servidor.
# La idea aquí es: uso la misma view, cuando la petición sea get, me muestra un formulario vacío para ser llenado. 
# Luego de llenar el formulario, cambio la petición de get a post para recibir los datos y guardarlos en la DB, es decir, hago el alta.

# Cleaned data es un diccionario que tiene los datos del formulario limpios, se asegura de que los datos son correctos. 

def buscar_curso(request):
    return render(request , "inicio.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        # De mi modelo curso quiero todos los objetos de tipo curso que tenga en la base de datos, pero filtrados si el nombre contiene el nombre que viene del formulario de búsqueda. 
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render(request , "resultado_busqueda.html" , {"cursos" : cursos})
        
    else:
        
        # return HttpResponse("Ingrese el nombre del curso")
        return render(request , "inicio.html")
    
def eliminar_curso(request , id):
    
    curso = Curso.objects.get(id = id)
    curso.delete()       
    
    curso = Curso.objects.all()
    
    return render(request , "cursos.html" , {"cursos" : curso}) 

def editar_curso(request , id):
    
    curso = Curso.objects.get(id = id)
    
    if request.method == "POST":
    
        mi_formulario = Curso_formulario(request.POST)
        
        if mi_formulario.is_valid():
            
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()
            
            curso = Curso.objects.all()
    
        return render( request , "cursos.html" , {"cursos" : curso})
    
    else:
        
        mi_formulario = Curso_formulario(initial = {"nombre" : curso.nombre ,"camada" : curso.camada})
    
    return render(request , "editar_curso.html" , {"mi_formulario" : mi_formulario , "curso" : curso})
    

def alta_profesor(request , nombre , apellido , curso):
    
    profesor = Profesor(nombre = nombre.title() , apellido = apellido.title() , curso = curso.title())
    profesor.save()
    texto = f"Se guardó en la Base de Datos el Profesor: {profesor.nombre} {profesor.apellido}. Curso de {profesor.curso}"
    
    return HttpResponse(texto)

def ver_profesores(request):
    
    profesores = Profesor.objects.all()
    diccionario = {"profesores" : profesores}
    plantilla = loader.get_template("profesores.html")
    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)


def profesor_formulario(request):
    
    if request.method == "POST":
        
        mi_formulario = Profesor_formulario(request.POST)
        
        if mi_formulario.is_valid():
            
            datos = mi_formulario.cleaned_data
            curso_id = datos["curso"]
            nombre_curso = Curso.objects.get(pk=curso_id).nombre
            profesor = Profesor(nombre=datos["nombre"].title(), apellido=datos["apellido"].title(), curso=nombre_curso.title())
            profesor.save()
            
            return render(request, "form_profesores.html")
        
    else:
        
        cursos = Curso.objects.all()  
        return render(request, "form_profesores.html", {"cursos": cursos})
    

