from django.urls import path
from .views import Menuprofessorview, reservarespacofisico

urlpatterns = [
    path('menuprofessor/', Menuprofessorview.as_view(), name='menuprofessor'),
    path('reservarespacofisico/', reservarespacofisico, name='reservarespacofisico'),
]
