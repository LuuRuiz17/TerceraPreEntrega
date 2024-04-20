from django.shortcuts import render
from django.shortcuts import redirect
from AppCoder.models import Curso, Avatar
from AppCoder.models import Alumno
from AppCoder.models import Profesor
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import Curso_formulario , UserEditForm
from .forms import Profesor_formulario
from .forms import Alumno_formulario
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.decorators import login_required



# Create your views here.

# model Alumno

def login_request(request):
    
    if request.method == "POST":
        
        form = AuthenticationForm(request , data = request.POST)
        
        if form.is_valid():
            # cleaned data retorna un diccionario
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username = usuario , password = contra)
            # autheticate: Si existe el usuario me retona un objeto usuario, y si no existe retorna "None"            
            if user is not None:
                
                login(request , user)
                avatares = Avatar.objects.filter(user = request.user.id)
                return render(request , "inicio.html" , {"url" : avatares[0].imagen.url , "usuario" : usuario})
            
            else: 
                 
                return HttpResponse("Usuario no encontrado.")
            
        else:
            return render(request , "login.html")
            
        
    form = AuthenticationForm()
    return render(request , "login.html" , {"form" : form})


def editar_perfil(request):
    
    usuario = request.user    
    
    if request.method == "POST":   
              
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request , "inicio.html")
    
    else: 
        
        miFormulario = UserEditForm(initial = {'email': usuario.email})
        
    return render(request , "editar_perfil.html" , {"miFormulario" : miFormulario , "usuario" : usuario})

def alta_alumno(request , nombre , apellido , email , contraseña):
    
    alumno = Alumno(nombre = nombre.title() , apellido = apellido.title() , email = email , contraseña = contraseña)
    alumno.save()
    texto = f"Se guardó en la Base de Datos el Alumno: {alumno.nombre} {alumno.apellido}"
    return HttpResponse(texto)

@login_required
def ver_alumnos(request):
    
    alumnos = Alumno.objects.all()
    diccionario = {"alumnos" : alumnos}
    plantilla = loader.get_template("alumnos.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def buscar_alumno(request):
    return render(request , "principal.html")

def resultado_alumno(request):
    if "nombre" in request.GET:
        nombre = request.GET.get("nombre", "")
        print("Nombre buscado:", nombre)  # Debugging: Imprime el nombre buscado
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
        print("Alumnos encontrados:", alumnos)  # Debugging: Imprime los alumnos encontrados
        return render(request, "resultado_alumnos.html", {"alumnos": alumnos})
    else:
        return redirect("buscar_alumno")


def alumno_formulario(request):
    
    if request.method == "POST":
        
        mi_formulario = Alumno_formulario(request.POST)
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno(nombre = datos["nombre"].title() , apellido = datos["apellido"].title() , email = datos["email"] , contraseña = datos["contraseña"])
            alumno.save()
            
            return render(request , "form_alumno.html")
            
    return render(request , "form_alumno.html") 


def eliminar_alumno(request , id):
    
    alumno = Alumno.objects.get(id = id)
    alumno.delete()       
    
    alumno = Alumno.objects.all()
    
    return render(request , "alumnos.html" , {"alumnos" : alumno}) 
    
    
def principal(request):
    logout(request)
    return render(request , "principal.html")  
 
    
def alta_curso(request, nombre , camada):
    curso = Curso(nombre = nombre.title() , camada = camada)
    curso.save()
    texto = f"Se guardó en la Base de Datos el Curso {curso.nombre} {curso.camada}"
    return HttpResponse(texto)


@login_required
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
    return render(request , "principal.html")

def resultado_curso(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        # De mi modelo curso quiero todos los objetos de tipo curso que tenga en la base de datos, pero filtrados si el nombre contiene el nombre que viene del formulario de búsqueda. 
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render(request , "resultado_busqueda.html" , {"cursos" : cursos})
        
    else:
        
        # return HttpResponse("Ingrese el nombre del curso")
        return render(request , "principal.html")
    
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

@login_required
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

def eliminar_profesor(request , id):
    
    profesor = Profesor.objects.get(id = id)
    profesor.delete()       
    
    profesor = Profesor.objects.all()
    
    return render(request , "profesores.html" , {"profesores" : profesor}) 