from django.urls import path
from .views import Cadastrardisciplinaview

urlpatterns = [
    path('cadastrardisciplina/', Cadastrardisciplinaview.cadastrar_disciplina ,name='cadastrardisciplina')
]
