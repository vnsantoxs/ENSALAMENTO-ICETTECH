from django.urls import path
from .views import Cadastrargradeview

urlpatterns = [
    path('cadastrargrade/', Cadastrargradeview.as_view(), name='cadastrargrade'),
]
