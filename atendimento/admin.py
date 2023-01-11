from django.contrib import admin

from produto.models import Produto
from servico.views import AtendimentoUpDateView
from .forms import AtendimentoListForm
from .models import Atendimento

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ['horario', 'cliente', 'funcionario', 'servico', 'situacao']
    search_fields = ('Cliente', 'funcionario')
    list_filter = ('horario', 'servico', 'situacao',)

    def save_model(self, request, obj, form, change):
        if obj.situacao == 'R':
            for produto in obj.servico.produtos:
                prd = Produto.objects.get(id=produto.produto.id)
                prd.quantidade -= produto.qtd
                prd.save()
        super().save_model(request, obj, form, change)


    def post(self, request, *args, **kwargs):
        form = AtendimentoListForm(self.request.POST)
        if form.is_valid():
            servico = form.cleaned_data.get('servico')
            situacao = form.cleaned_data.get('situacao')
            if situacao == 'R':
                for produto in servico.produtos:
                  prd = Produto.objects.get(id=produto.produto.id)
                  prd.quantidade -= produto.qtd
                  prd.save()

        return super(AtendimentoUpDateView, self).post(request, *args, **kwargs)
