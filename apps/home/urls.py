"""Home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import CreditosView,HomeView,formularioView,ListarAccesorios,RegistroView,LoginView
app_name='app1'
urlpatterns = [
    path('creditos/', CreditosView.as_view(), name='creditos'),
    path('home/', HomeView.as_view(), name='home'),
    path('formulario/', formularioView.as_view(), name='formulario'),
    path('listado/', ListarAccesorios.as_view(), name='listado'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
    
]
