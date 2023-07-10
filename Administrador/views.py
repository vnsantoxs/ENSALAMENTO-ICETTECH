from django.shortcuts import render
from django.views.generic import TemplateView
from Curso.models import Curso
from Grade.models import Grade
from EspacoFisico.models import EspacoFisico
from Disciplina.models import Disciplina
from Aplicacao.models import Feedback
from Administrador.models import Administrador
from Professor.models import Professor
from Alocacao.models import Alocacao

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
    def allfeedbackview(request):
        return render(request, 'v.feedback1.html')
    
    def feedbackview(request):
        return render(request, 'v.feedback2.html')


def Gerarensalamentoview(request):
    disciplina =  Disciplina.objects.all()
    professor = Professor.objects.all()
    alocacoes = Alocacao.objects.order_by('professor')
    return render(request, 'gerar_ensalamento.html', {'disciplina': disciplina, 'professor': professor, 'alocacoes':alocacoes})


class visualizarensalamento(TemplateView):
    def visualizarensalamentoview(request):
        alocacoes = Alocacao.objects.order_by('horario_alocacao')
        return render(request, 'visualizar_Ensalamento.html', {'alocacoes':alocacoes})
    

class Visualizarresevaview(TemplateView):
    def visualizarreservas(request):
        return render(request, 'v.reserva1.html')
    
    def visualizarreserva(request):
        return render(request, 'v.Reserva2.html')
    
class Visualizarusuarioview(TemplateView):
    def visualizarusuario(request, professor_id):
        usuario = Professor.objects.get(id_professor=professor_id)
        return render(request, 'v.usuario1.html', {'usuario': usuario})


    def visualizarusuarios(request):
        professor = Professor.objects.all()
        return render(request, 'visualizar_Usuаrio.html', {'professor':professor})  
