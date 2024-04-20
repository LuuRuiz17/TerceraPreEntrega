from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path("" , views.principal , name = "principal"),
     
    # model Curso
    path("login" , views.login_request, name = "login"),
    path("logout" , LogoutView.as_view(template_name = "logout.html") , name = "Logout"),
    
    path("alta_curso" , views.curso_formulario, name = "alta_curso"),  
    path("ver_cursos" , views.ver_cursos , name = "cursos"),
    path("buscar_curso" , views.buscar_curso , name = "buscar_curso"),
    path("resultado_curso" , views.resultado_curso , name = "resultado_curso"),
    path("eliminar_curso/<int:id>" , views.eliminar_curso , name = "eliminar_curso"),
    path("editar_curso/<int:id>" , views.editar_curso , name = "editar_curso"),
    
    # model Alumno

    path("alta_alumno" , views.alumno_formulario , name = "alta_alumno"),
    path("ver_alumnos" , views.ver_alumnos , name = "alumnos"),
    path("buscar_alumno" , views.buscar_alumno , name = "buscar_alumno"),
    path("resultado_alumno" , views.resultado_alumno , name = "resultado_alumno"),
    path("editar_perfil" , views.editar_perfil , name = "editar_perfil"),
    path("eliminar_alumno/<int:id>" , views.eliminar_alumno , name = "eliminar_alumno"),
    
    # model Profesor
    
    path("alta_profesor" , views.profesor_formulario , name = "alta_profesor"),
    path("ver_profesores" , views.ver_profesores , name = "profesores"),
    path("eliminar_profesor/<int:id>" , views.eliminar_profesor , name = "eliminar_profesor"),
    path("editar_profesor/<int:id>" , views.editar_profesor , name = "editar_profesor")
]
