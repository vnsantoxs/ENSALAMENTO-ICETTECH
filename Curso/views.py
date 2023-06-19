from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Curso

class cadastrarcursoview(TemplateView):
    def cadastrar_curso(request):
        if request.method == 'POST':
            codigo = request.POST.get('codigo')
            nome = request.POST.get('nome')
            curso = Curso.cadastrarCurso(codigo=codigo, nome=nome)
            if curso:
                return render(request,'cadastro_curso.html')
            else: 
                return render(request, 'cadastro_curso.html')
        else:
            return render(request, 'cadastro_curso.html')