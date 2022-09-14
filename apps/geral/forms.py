from django import forms
from .models import Categoria
from django.contrib.auth.models import User


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        # somente os campos que preciso exibir
        fields = ['nome', 'tipo', 'descricao']
        # fields = '__all__'
        # exclude = ['usuario']


class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário', required=True)
    password = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput())


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
