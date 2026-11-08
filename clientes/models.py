from django.db import models

class Cliente(models.Model):
    nome = models.CharField('nome', max_length=120)
    telefone = models.CharField('telefone', max_length=20)
    email = models.EmailField('e-mail', blank=True)
    endereco = models.CharField('endereço', max_length=255, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.nome
