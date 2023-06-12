from django.shortcuts import render
from django.views.generic import TemplateView

class Cadastrardisciplinaview(TemplateView):
    template_name = 'cadastro_disciplina.html'