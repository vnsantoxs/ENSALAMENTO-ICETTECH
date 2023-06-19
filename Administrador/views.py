from django.shortcuts import render
from django.views.generic import TemplateView
from Curso.models import Curso
from Grade.models import Grade
from EspacoFisico.models import EspacoFisico
from Disciplina.models import Disciplina
from Aplicacao.models import Feedback

class gerennciamento(TemplateView):
    template_name = 'funcao_Gerenciamento.html'

    def gerenciamentocurso(request):
        cursos = Curso.objects.all()
        return render(request,'G_curso.html',{'cursos': cursos})
    
    def gerenciamentodisciplina(request):
        disciplina = Disciplina.objects.all()
        return render(request, 'G_disciplina.html', {'disciplina': disciplina})
    
    def gerenciamentoespacofisico(request):
        espacofisico = EspacoFisico.objects.all()
        return render(request, 'G_espaЗo-fisico.html', {'espacofisico': espacofisico})
    
    def gerenciamentograde(request):
        grade = Grade.objects.all()
        return render(request, 'G_grade.html', {'grade': grade})
    
class feedbackviews(TemplateView):
    def feedbackview(request):
        feedback = Feedback.objects.all()
        return render(request, 'visualizar_Feedback.html', {'feedback': feedback})
    
