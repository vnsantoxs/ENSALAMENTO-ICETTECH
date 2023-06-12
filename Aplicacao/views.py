from django.shortcuts import render
from django.views.generic import TemplateView
from Administrador.models import Administrador
from Professor.models import Professor
import os
from pathlib import Path

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
    template_name = 'cadastro_Professor.html'

class Registrarfeedbackview(TemplateView):
    template_name = 'registrar_Feedback.html'