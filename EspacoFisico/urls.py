from django.urls import path
from .views import Cadastrarespacofisicoview

urlpatterns = [
    path('cadastrarespacofisico/', Cadastrarespacofisicoview.as_view(), name='cadastrarespacosisico'),
]
