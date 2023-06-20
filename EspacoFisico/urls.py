from django.urls import path
from .views import Cadastrarespacofisicoview

urlpatterns = [
    path('cadastrarespacofisico/', Cadastrarespacofisicoview.cadastrar_espaco_fisico, name='cadastrarespacosisico'),
]
