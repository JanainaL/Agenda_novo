from django.contrib import admin
from .models import Atendimento

@admin.register(Atendimento)
class Atendimento(admin.ModelAdmin):
    list_display = ('horario', 'cliente', 'funcionario', 'servico', 'situacao')
    search_fields = ('Cliente', 'funcionario')
    list_filter = ('horario', 'servico', 'situacao')