from django.shortcuts import render
from django.views.generic import TemplateView
from .models import EspacoFisico

class Cadastrarespacofisicoview(TemplateView):
    def cadastrar_espaco_fisico(request):
        if request.method == 'POST':
            dimensoes = request.POST.get('dimensoes')
            capacidade = request.POST.get('capacidade')
            andar = request.POST.get('andar')
            numero = request.POST.get('numero')
            nome_bloco = request.POST.get('nome_bloco')
            tipo = request.POST.get('tipo_EF')

            espaco_fisico = EspacoFisico.cadastrarEspacoFisico(dimensoes=dimensoes,capacidade=capacidade,bloco=nome_bloco,
                                                               andar=andar, numero=numero, tipo_espaco_fisico=tipo)
            if espaco_fisico:
                return render(request, 'cadastro_espacofisico.html')
            else:
                return render(request, 'cadastro_espacofisico.html')
        else:
            return render(request, 'cadastro_espacofisico.html')
