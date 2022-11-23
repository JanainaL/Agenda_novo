from django.contrib import admin
from produto.models import Produto
from produtoservico.models import ProdutoServico
from .models import Servico

class ProdutoServicoInLine(admin.TabularInline):
    model = ProdutoServico
    extra = 1

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'preco', 'get_produtos']
    inlines = [ProdutoServicoInLine]
    search_fields = ('nome', 'descricao')


    def get_produtos(self, obj):
        return ', '.join([prd.nome for prd in Produto.objects.filter(servico=obj.id)])

    get_produtos.short_description = "Produtos Utilizados"