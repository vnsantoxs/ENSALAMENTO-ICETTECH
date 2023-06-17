from django.shortcuts import render
from django.views.generic import TemplateView

class gerennciamento(TemplateView):
    template_name = 'funcao_Gerenciamento.html'

    def gerenciamentocurso(request):
        return render(request,'G_curso.html')
    
    def gerenciamentodisciplina(request):
        return render(request, 'G_disciplina.html')
    
    def gerenciamentoespacofisico(request):
        return render(request, 'G_espaЗo-fisico.html')
    
    def gerenciamentograde(request):
        return render(request, 'G_grade.html')
    
class feedbackview(TemplateView):
    template_name = 'visualizar_Feedback.html'
    
