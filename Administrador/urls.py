from django.urls import path
from .views import Menuadministradorview

urlpatterns = [
    path('menuadministrador/', Menuadministradorview.as_view(), name='menuadministrador'),
]
