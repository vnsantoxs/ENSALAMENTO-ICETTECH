from django.contrib import admin
from .models import Administrador
from Curso.models import Curso
from Disciplina.models import Disciplina
from EspacoFisico.models import EspacoFisico
from Professor.models import Professor
from Grade.models import Grade
from Alocacao.models import Alocacao

admin.site.register(Administrador)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(EspacoFisico)
admin.site.register(Professor)
admin.site.register(Grade)
admin.site.register(Alocacao)
