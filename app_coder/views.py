from gettext import textdomain
from django.shortcuts import render
from django.http import HttpResponse
from app_coder.models import Curso, Profesor, Alumno
from django.template import loader
from app_coder.forms import Curso_formulario , Alumno_formulario , Profesor_formulario


# Create your views here.

def inicio(request):

    return render (request, "plantillas.html")

def cursos (request):
    cursos = Curso.objects.all()
    dicc = {"cursos" : cursos}
    plantilla = loader.get_template ("plantillas.html")
    documento = plantilla.render(dicc)
    return HttpResponse ( documento )

def alta_curso (request, nombre):
    curso = curso( nombre=nombre, camada=28787554)
    curso.save()
    texto = f"Se guardo en la BD el Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(texto)

def alumnos (request):

    return render( request , "alumnos.html")

def contacto (request):

    return render( request , "contacto.html")

def profesores (request):

    return render( request , "profesores.html")



    
def curso_formulario (request):

    if request.method == "POST":

        mi_formulario = Curso_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            curso = curso( nombre=datos['nombre'], camada=datos['camada'])
            curso.save

            return render( request , "formulario.html")
    return render( request , "formulario.html")


def alta_profesores (request):

    if request.method == "POST":

        mi_formulario = Profesor_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            profesor = Profesor( nombre=datos['nombre'], legajo=datos['legajo'])
            profesor.save

            return render( request , "formulario.html")
    return render( request , "alta_profesores.html")


def alta_alumnos (request):

    if request.method == "POST":

        mi_formulario = Alumno_formulario( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            alumno = Alumno( nombre=datos['nombre'], apellido=datos['apellido'], )
            alumno.save

            return render( request , "formulario.html")
    return render( request , "alta_alumnos.html")    

def buscar_curso (request):

    return render( request , "buscar_curso.html")


def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET ['nombre']
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render(request, "resultado_busqueda.html" , {"cursos": cursos})
    else:
        return HttpResponse ("Campo vacio")

