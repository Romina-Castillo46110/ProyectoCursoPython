from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.inicio, name="home"),
    path("ver_cursos", views.ver_cursos , name="cursos"),
    path("ver_alumnos", views.ver_alumnos , name="alumnos"),
    path("ver_profesores", views.ver_profesores , name="profesores"),
    path("alta_curso", views.curso_formulario),
    path("alta_profesor", views.profesor_formulario),
    path("alta_alumno", views.alumno_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscarCurso", views.buscarCurso),
    path("buscar_alumno", views.buscar_alumno),
    path("buscarAlumno", views.buscarAlumno),
    path("buscar_profesor", views.buscar_profesor),
    path("buscarProfesor", views.buscarProfesor),
    path("eliminar_curso/<int:id>", views.eliminar_curso, name="eliminar_curso"),
    path("eliminar_profesor/<int:id>", views.eliminar_profesor, name="eliminar_profesor"),
    path("eliminar_alumno/<int:id>", views.eliminar_alumno, name="eliminar_alumno"),
    path("editar_curso/<int:id>", views.editar, name="editar_curso"),
    path("editar_profesor/<int:id>", views.editar_profesor, name="editar_profesor"),
    path("editar_alumno/<int:id>", views.editar_alumno, name="editar_alumno"),
    path("login", views.login_request , name="login"),
    path("register", views.register , name="register"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("editarPerfil", views.editarPerfil, name="editarPerfil")

]

'''
buscar, eliminar, crear, modificar (CRUD)
PROFESOR: ALTA PROFESOR, BUSCAR PROFESOR
ALUMNO: ALTA ALUMNO, BUSCAR ALUMNO,
CURSO: ALTA CURSO, BUSCAR CURSO, ELIMINAR CURSO, EDITAR CURSO
'''