from django.shortcuts import render
from django.views.generic import TemplateView
from .models import EspacoFisico

class Cadastrarespacofisicoview(TemplateView):
    def cadastrar_espaco_fisico(request):
        if request.method == 'POST':
            tipo_espaco_fisico = request.POST.get('tipo_espaco_fisico')
            dimensoes = request.POST.get('dimensoes')
            capacidade = request.POST.get('capacidade')
            bloco = request.POST.get('bloco')
            andar = request.POST.get('andar')
            numero = request.POST.get('numero')
            nome_bloco = request.POST.get('nome_bloco')

            espaco_fisico = EspacoFisico.cadastrarEspacoFisico(tipo_espaco_fisico=tipo_espaco_fisico,
                                                                dimensoes=dimensoes, capacidade=capacidade,
                                                                bloco=bloco, andar=andar,
                                                                numero=numero, nome_bloco=nome_bloco)
            if espaco_fisico:
                return render(request, 'cadastro_espacofisico.html')
            else:
                return render(request, 'cadastro_espacofisico.html')
        else:
            return render(request, 'cadastrar_espaco_fisico.html')
