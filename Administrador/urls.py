from django.urls import path
from .views import gerennciamento, feedbackviews, Gerarensalamento, Visualizarresevaview, Visualizarusuarioview

urlpatterns = [
    path('gerenciamento/', gerennciamento.as_view(), name='gerenciamento'),
    path('visualizarallfeedback/', feedbackviews.allfeedbackview, name='visualizarallfeedback'),
    path('vizualizarfeedback/', feedbackviews.feedbackview, name='vizualizarfeedback'),
    path('gerenciamento/curso/', gerennciamento.gerenciamentocurso, name='gerenciamentocurso'),
    path('gerenrenciamento/disiciplina/', gerennciamento.gerenciamentodisciplina, name='gerenrenciamentodisiciplina'),
    path('gerenciamento/espacofisico/', gerennciamento.gerenciamentoespacofisico, name='gerenciamentoespacofisico'),
    path('gerenciamento/grade/', gerennciamento.gerenciamentograde, name='gerenciamentograde'),
    path('gerarensalamento/', Gerarensalamento.as_view(), name='gerarensalamento'),
    path('visualizarreservas/', Visualizarresevaview.visualizarreservas, name= 'visualizarreservas'),
    path('visualizarreserva/', Visualizarresevaview.visualizarreserva, name= 'visualizarreserva'),
    path('visualizarusuarios/', Visualizarusuarioview.visualizarusuarios, name='visualizarusuarios'),
    path('visualizarusuario/', Visualizarusuarioview.visualizarusuario, name='visualizarusuario'),
]
