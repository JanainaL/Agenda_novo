from django import forms

from atendimento.models import Atendimento
from cliente.models import Cliente
from funcionario.models import Funcionario
from servico.models import Servico

class AtendimentoListForm(forms.Form):
    SITUACAO_OPCOES = (
        ('T', '----------'),
        ('A', 'Agendado'),
        ('R', 'Realizado'),
        ('C', 'Cancelado')
    )

    cliente = forms.ModelChoiceField(label='Cliente:', widget=forms.Select(attrs={'class': 'select is-fullwidth '}), queryset=Cliente.objects.all(), required=False )

    funcionario = forms.ModelChoiceField(label='Funcionário:', widget=forms.Select(attrs={'class': 'select is-fullwidth'}), queryset=Funcionario.objects.all(), required=False)

    servico = forms.ModelChoiceField(label='Servico:', widget=forms.Select(attrs={'class': 'select is-fullwidth'}), queryset=Servico.objects.all(), required=False)

    situacao = forms.ChoiceField(label='Situação:', widget=forms.Select(attrs={'class': 'select is-fullwidth'}), choices=SITUACAO_OPCOES, required=False)
class AtendimentoModelForm(forms.ModelForm):
    class Meta:
      model = Atendimento
      fields = ['horario', 'cliente', 'funcionario', 'servico', 'situacao']
      widgets ={
          'horario': forms.DateTimeInput(
              attrs={'class': 'input', 'type':'text', 'placeholder':'Digite o horario'}),
          'cliente': forms.Select(
              attrs={'class':'input','type':'text', 'placeholder':'Selecione o cliente'}),
          'funcionario':forms.Select(
              attrs={'class': 'input', 'type': 'text', 'placeholder': 'Selecione o funcionário'}),
          'servico': forms.Select(
              attrs={'class': 'input', 'type': 'text', 'placeholder': 'Selecione o serviço'}),
          'situacao': forms.Select(
              attrs={'class': 'input', 'type': 'text', 'placeholder': 'Selecione a situação'}),
      }
