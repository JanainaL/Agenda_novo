from django.db import models

class ProdutoServico(models.Model):
    servico = models.ForeignKey('servico.Servico', verbose_name='Serviço', help_text='Nome do serviço realizado', on_delete=models.CASCADE, related_name='servico')
    produto = models.ForeignKey('produto.Produto', verbose_name='produto', help_text='Nome do produto', on_delete=models.CASCADE, related_name='produto')
    qtd = models.DecimalField('Quantidade', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Produto utilizado'
        verbose_name_plural = 'Produtos utilizados'

    def __str__(self):
        return f'{self.produto}'
