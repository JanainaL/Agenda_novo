from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

from .forms import FuncionarioModelForm
from .models import Funcionario

class FuncionariosView(ListView):
    model = Funcionario
    template_name = 'funcionarios.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(FuncionariosView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        paginator = Paginator(qs, 1)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = 'funcionario_apagar.html'
    success_url = reverse_lazy('funcionarios')

class FuncionarioAddView(CreateView):
        form_class = FuncionarioModelForm
        model = Funcionario
        template_name = 'funcionario_form.html'
        success_url = reverse_lazy('funcionarios')


class FuncionarioUpDateView(UpdateView):
    form_class = FuncionarioModelForm
    model = Funcionario
    template_name = 'funcionario_form.html'
    success_url = reverse_lazy('funcionarios')


class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = 'funcionario_apagar.html'
    success_url = reverse_lazy('funcionarios')