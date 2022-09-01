from django import forms
from .models import Categoria


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        # somente os campos que preciso exibir
        fields = ['nome', 'tipo', 'descricao']
        # fields = '__all__'
        # exclude = ['usuario']
