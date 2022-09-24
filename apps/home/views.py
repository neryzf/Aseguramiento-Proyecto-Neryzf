from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView
from .forms import productoForm,RegistroForm
from .models import Usuario, producto
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
# Create your views here.

class CreditosView(TemplateView):
    template_name='creditos.html'

class HomeView(TemplateView):
    template_name='index.html'

class formularioView(CreateView):
    template_name= 'formulario.html'
    form_class = productoForm
    success_url = reverse_lazy('app1:listado')

class ListarAccesorios(ListView):
    template_name = 'listado.html'
    model = producto

    def get_queryset(self):
        return producto.objects.all()

class RegistroView(CreateView):
    model = Usuario
    form_class = RegistroForm
    success_url = reverse_lazy('app1:login')

class LoginView(LoginView):
    template_name = 'login.html'

