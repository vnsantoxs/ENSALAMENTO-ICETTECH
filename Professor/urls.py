from django.urls import path
from .views import Menuprofessorview

urlpatterns = [
    path('menuprofessor/', Menuprofessorview.as_view(), name='menuprofessor'),
]
