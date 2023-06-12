from django.shortcuts import render
from django.views.generic import TemplateView

class cadastrarcursoview(TemplateView):
    template_name = 'cadastro_curso.html'