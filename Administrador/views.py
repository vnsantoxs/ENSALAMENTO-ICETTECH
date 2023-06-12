from django.shortcuts import render
from django.views.generic import TemplateView

class Menuadministradorview(TemplateView):
    template_name = 'menu_Admin.html'