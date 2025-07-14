"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
# path é usado para definir os caminhos das URLs
# A função path() espera pelo menos dois argumentos: route e view. 
# Importa o include para incluir urls de outros aplicativos
# A função include() permite referenciar outros URLconfs.

urlpatterns = [
    # caminho padrão do django para exibir o administrador
    path('admin/', admin.site.urls),
    # ceria um caminho para o aplicativo polls
    path('polls/', include('polls.urls')),
]
