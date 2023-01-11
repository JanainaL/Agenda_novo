from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateResponseMixin, View

from atendimento.forms import AtendimentoModelForm
from atendimento.models import Atendimento
from .forms import ProdutoServicoInLine
from .models import Servico

class ServicosView(ListView):
    model = Servico
    template_name = 'servicos.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ServicosView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(Q(nome__icontains=buscar) | Q(descricao__icontains=buscar))

        paginator = Paginator(qs, 1)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem
class ServicoInLineEditView(TemplateResponseMixin, View):
    template_name = 'servico_form_inline.html'
    servico = None

    def get_formset(self, data=None):
        return ProdutoServicoInLine(isinstance=self.servico, data=data)

    def dispatch(self, request, pk):
        self.servico = get_object_or_404(Servico, id=pk)
        return super().dispatch(request, pk)
    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'servico': self.servico, 'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('servicos')
        return self.render_to_response({'servico': self.servico, 'formset': formset})

class AtendimentoAddView(CreateView):
    form_class = AtendimentoModelForm
    model = Atendimento
    template_name = 'atendimento_form.html'
    success_url = reverse_lazy('atendimentos')

class AtendimentoUpDateView(UpdateView):
    form_class = AtendimentoModelForm
    model = Atendimento
    template_name = 'atendimento_form.html'
    success_url = reverse_lazy('atendimentos')

class AtendimentoDeleteView(DeleteView):
    model = Atendimento
    template_name = 'atendimento_apagar.html'
    success_url = reverse_lazy('atendimentos')