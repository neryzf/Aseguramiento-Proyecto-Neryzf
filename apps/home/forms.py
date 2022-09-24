from django import forms 
from .models import producto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class productoForm(forms.ModelForm):
    class Meta:
        model=producto
        fields='__all__'

class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=140,required=True)
    last_name = forms.CharField(max_length=140,required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )