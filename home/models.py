from django.db import models
from stdimage import StdImageField

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text="Nome Completo")
    fone = models.CharField('Telefone', max_length=15, help_text="Número do telefone")
    email = models.EmailField("E-mail", max_length=100, help_text="Endereço de e-mail", unique=True)
    foto = StdImageField('Foto', upload_to='pessoas', variations={'thumbnail': {'width': 100, 'height': 100,
                                                                                'crop': True}}, delete_orphans=True, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome
