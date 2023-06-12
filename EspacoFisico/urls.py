from django.urls import path
from .views import Cadastrarespacofisicoview

urlpatterns = [
    path('cadastrarespacosisico/', Cadastrarespacofisicoview.as_view(), name='cadastrarespacosisico'),
]
