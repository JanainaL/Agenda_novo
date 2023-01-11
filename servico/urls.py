from django.urls import path
from .views import ServicosView, ServicoInLineEditView

urlpatterns = [
    path('servicos', ServicosView.as_view(), name='servicos'),
    path('<int:pk>/servico/inline', ServicoInLineEditView.as_view(), name='servico_inline'),
]