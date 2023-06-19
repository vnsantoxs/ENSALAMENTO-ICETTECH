from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Disciplina

class Cadastrardisciplinaview(TemplateView):
    def cadastrar_disciplina(request):
        if request.method == 'POST':
            codigo = request.POST.get('nome')
            nome = request.POST.get('codigo')
            periodo = request.POST.get('periodo')
            disciplina = Disciplina.cadastrarDisciplina(codigo=codigo, nome=nome, periodo_disciplina=periodo)
            if disciplina:
                return render(request,'cadastro_disciplina.html')
        else:
            return render(request, 'cadastro_disciplina.html')