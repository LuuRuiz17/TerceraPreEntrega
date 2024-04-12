from django.urls import path
from . import views

urlpatterns = [
   path("" , views.inicio , name = "inicio"),
     
    # model Curso
    
    path("alta_curso" , views.curso_formulario, name = "alta_curso"),  
    path("ver_cursos" , views.ver_cursos , name = "cursos"),
    path("buscar_curso" , views.buscar_curso , name = "buscar_curso"),
    path("buscar" , views.buscar , name = "buscar"),
    path("eliminar_curso/<int:id>" , views.eliminar_curso , name = "eliminar_curso"),
    path("editar_curso/<int:id>" , views.editar_curso , name = "editar_curso"),
    
    # model Alumno

    path("alta_alumno" , views.alumno_formulario , name = "alta_alumno"),
    path("ver_alumnos" , views.ver_alumnos , name = "alumnos"),
    
    # model Profesor
    
    path("alta_profesor" , views.profesor_formulario , name = "alta_profesor"),
    path("ver_profesores" , views.ver_profesores , name = "profesores")
]
