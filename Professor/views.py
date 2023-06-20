from django.shortcuts import render
from django.views.generic import TemplateView


class Menuprofessorview(TemplateView):
    template_name =  'menu_Professor.html'

def reservarespacofisico(request):
    return render(request, 'Reserva.html')