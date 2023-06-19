from django.urls import path
from .views import gerennciamento, feedbackviews

urlpatterns = [
    path('gerenciamento/', gerennciamento.as_view(), name='gerenciamento'),
    path('visualizarfeedback/', feedbackviews.feedbackview, name='visualizarfeedback'),
    path('gerenciamento/curso/', gerennciamento.gerenciamentocurso, name='gerenciamentocurso'),
    path('gerenrenciamento/disiciplina/', gerennciamento.gerenciamentodisciplina, name='gerenrenciamentodisiciplina'),
    path('gerenciamento/espacofisico/', gerennciamento.gerenciamentoespacofisico, name='gerenciamentoespacofisico'),
    path('gerenciamento/grade/', gerennciamento.gerenciamentograde, name='gerenciamentograde'),
]
