from django import forms

from .models import Produto

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preço', 'fornecedor', 'quantidade']
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do produto'}),
            'preco': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o preço do produto'}),
            'fornecedor': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o fornecedor'}),
            'quantidade': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a quantidade'}),

        }