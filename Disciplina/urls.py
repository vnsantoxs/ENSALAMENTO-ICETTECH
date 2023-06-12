from django.urls import path
from .views import Cadastrardisciplinaview

urlpatterns = [
    path('cadastrardisciplina/', Cadastrardisciplinaview.as_view(), name='cadastrardisciplina')
]
