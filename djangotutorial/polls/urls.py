# de django urls importe o caminho
from django.urls import path
# Importa as views do módulo atual
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]