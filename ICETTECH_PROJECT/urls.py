from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Aplicacao.urls')),
    path('', include('Administrador.urls')),
    path('', include('Curso.urls')),
    path('', include('Disciplina.urls')),
    path('', include('EspacoFisico.urls')),
    path('', include('Professor.urls')),
    path('', include('Grade.urls')),
]
