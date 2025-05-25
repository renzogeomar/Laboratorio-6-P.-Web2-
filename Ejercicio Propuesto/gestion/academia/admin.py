from django.contrib import admin

# Register your models here.
from .models import Alumno, Curso, NotaAlumnoPorCurso

admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(NotaAlumnoPorCurso)