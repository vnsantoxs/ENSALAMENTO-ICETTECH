from django.shortcuts import render
from django.views.generic import TemplateView

class Cadastrargradeview(TemplateView):
    template_name='cadastro_grade.html'