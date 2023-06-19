from django.urls import path
from .views import cadastrarcursoview

urlpatterns = [
    path('cadastrarcurso/', cadastrarcursoview.cadastrar_curso, name='cadastrarcurso')
]
