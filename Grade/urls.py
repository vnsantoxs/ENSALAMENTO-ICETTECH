from django.urls import path
from .views import Cadastrargradeview

urlpatterns = [
    path('cadastrargrade/', Cadastrargradeview.cadastrarGrede, name='cadastrargrade'),
]
