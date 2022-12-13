from django.urls import path
from .views import AtendimentosView

urlpatterns = [
    path('atendimentos', AtendimentosView.as_view(), name='atendimentos'),
]