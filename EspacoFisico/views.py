from django.shortcuts import render
from django.views.generic import TemplateView

class Cadastrarespacofisicoview(TemplateView):
    template_name='cadastro_espacofisico.html'
