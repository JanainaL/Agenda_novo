from django import forms
from django.forms import inlineformset_factory

from produtoservico.models import ProdutoServico
from servico.models import Servico

ProdutoServicoInLine = inlineformset_factory(Servico, ProdutoServico, fk_name='servico', fields=('produto', 'qtd'),
                                             extra=1, can_delete=True,
                                             widgets={'qtd':forms.NumberInput(attrs={'class': 'input', 'type': 'number'}),
                                                      'produto': forms.Select(attrs={'class': 'input'})})