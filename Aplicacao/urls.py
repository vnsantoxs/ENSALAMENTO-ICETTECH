from django.urls import path,include
from django.contrib.auth import views as auth_view
from .views import Indexview, Loginview,Tipocadastroview, Cadastroprofessorview, Registrarfeedbackview
import Aplicacao.views as Aplicacao


urlpatterns = [
    path('', Indexview.as_view(), name='index'),
    path('', include('Administrador.urls')),
    path('login/',Loginview.login, name='login'),
    path('tipocadastro/', Tipocadastroview.as_view(), name='tipocadastro'),
    path('cadastroadministrador/', Aplicacao.Cadastroadminview.cadastraradministrador, name='cadastroadministrador'),
    path('cadastroprofessor/', Cadastroprofessorview.cadastrarprofessor, name='cadastroprofessor'),
    path('registrarfeedback/',Registrarfeedbackview.registrarfeedback, name='registrarfeedback'),
    path('aboutus/', Aplicacao.aboutus, name='aboutus')
]
