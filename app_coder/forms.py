from django import forms

class Curso_formulario (forms.Form):
    nombre = forms.CharField(max_length=40)
    camada = forms.IntegerField()


class Alumno_formulario (forms.Form):
    nombre = forms.CharField (max_length=30)
    apellido = forms.CharField (max_length=30)
    email = forms.EmailField()

class Profesor_formulario (forms.Form):
    nombre = forms.CharField (max_length=30)
    legajo = forms.IntegerField()
