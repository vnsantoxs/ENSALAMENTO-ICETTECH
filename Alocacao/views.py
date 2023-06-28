from django.shortcuts import render

def salvar_alocacao(request):
    if request.method == 'POST':
        dia_semana = request.POST.get('dia')
        horario_alocacao = request.POST.get('horario')
        disciplina= request.POST.get('disciplina')
        espaco_fisico = request.POST.get('espaco_fisico')
        professor = request.POST.get('professor')

