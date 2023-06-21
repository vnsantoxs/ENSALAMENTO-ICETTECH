from django.shortcuts import render
from django.views.generic import TemplateView
from Administrador.models import Administrador
from Professor.models import Professor
import os
from pathlib import Path
from .models import Feedback

class Indexview(TemplateView):
    template_name = 'index.html'

class Tipocadastroview(TemplateView):
    template_name = 'tipocadastro.html'

class Loginview(TemplateView):
    def login(request):
        if request.method == 'GET':
            return render(request, 'Login.html')
        else:
            siape = request.POST.get('siape')
            senha = request.POST.get('senha')
            if Administrador.loginadmin(siape=siape,senha=senha):
                return render(request, 'menu_Admin.html')
            elif Professor.loginprofessor(siape=siape,senha=senha):
                return render(request, 'menu_Professor.html')
            else:
                return render(request, 'Login.html')
            
class Cadastroadminview(TemplateView):
    def cadastraradministrador(request):
        if request.method == 'GET':
            return render(request, 'cadastro_Admin.html')
        else: 
            nome = request.POST.get('Nome')
            telefone = request.POST.get('telefone')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            siape = request.POST.get('siape')
            cargo = request.POST.get('cargo')
            comorbidade = request.POST.get('comorbidade') == 'sim'

            admin = Administrador.cadastrar_Administrador(nome_administrador=nome, telefone_administrador=telefone,
                                                          email_administrador=email,senha_administrador=senha,
                                                          siape_administrador=siape,cargo_administrador=cargo,
                                                          comorbidade_administrador=comorbidade, estado_administrador=False)
            if admin:
                return render(request, 'Login.html')
            else:
                return render(request, 'index.html')

class Cadastroprofessorview(TemplateView):
    def cadastrarprofessor(request):
        if request.method == 'GET':
            return render(request, 'cadastro_Professor.html')
        else: 
            nome = request.POST.get('Nome')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            siape = request.POST.get('siape')
            area_atuacao = request.POST.get('area')
            comorbidade = request.POST.get('comorbidade')
            
            cadastro = Professor.cadastrar_Professor(nome_professor=nome, email_professor=email, senha_professor=senha, siape_professor=siape,
                                                    area_atuacao_professor=area_atuacao, comorbidade=comorbidade,  estado_professor=False)
            if cadastro:
                return render(request, 'Login.html')
            else:
                return render(request, 'index.html')


class Registrarfeedbackview(TemplateView):
    def registrarfeedback(request):
        if request.method == 'GET':
            return render(request, 'registrar_Feedback.html')
        else: 
            feed = request.POST.get('feedback')
            feedback = Feedback.salvarfeedback(feedback=feed)
            if feedback:
                return render(request, 'menu_Professor.html')
            else:
                return render(request, 'registrar_Feedback.html')

def aboutus(request):
    return render(request,'aboutus.html')

def perfilview(request):
    return render(request, 'Perfil_Usuаrio.html')