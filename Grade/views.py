from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Grade

class Cadastrargradeview(TemplateView):
    def cadastrarGrede(request):
        if request.method == 'POST':
            ano = request.POST.get('ano')
            versao = request.POST.get('versao')
            codigo = request.POST.get('codigo')

            grade = Grade.objects.create(ano=ano, versao=versao, codigo=codigo)
            if grade:
                return render(request, 'cadastro_grade.html')
            else:
                return render(request, 'cadastro_grade.html')
        else:
            return render(request, 'cadastro_grade.html')