from django.urls import path
from .views import cadastrarcursoview

urlpatterns = [
    path('cadastrarcurso/', cadastrarcursoview.as_view(), name='cadastrarcurso')
]
