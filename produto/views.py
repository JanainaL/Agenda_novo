from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import ProdutoModelForm
from .models import Produto

class ProdutosView(ListView):
    model = Produto
    template_name = 'produto.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ProdutosView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(Q(nome__icontains=buscar) | Q(descricao__icontains=buscar))

        paginator = Paginator(qs, 1)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem


class ProdutoAddView(CreateView):
    form_class = ProdutoModelForm
    model = Produto
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produtos')


class ProdutoUpDateView(UpdateView):
    form_class = ProdutoModelForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produtos')


class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produto_apagar.html'
    success_url = reverse_lazy('produtos')