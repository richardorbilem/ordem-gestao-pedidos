from django.db import models
from clientes.models import Cliente

class Pedido(models.Model):
    class Status(models.TextChoices):
        EM_ANALISE = 'em_analise', 'Em análise'
        EM_PRODUCAO = 'em_producao', 'Em produção'
        EM_INSTALACAO = 'em_instalacao', 'Em instalação'
        CONCLUIDO = 'concluido', 'Concluído'
        CANCELADO = 'cancelado', 'Cancelado'

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='pedidos', verbose_name='cliente')
    descricao = models.TextField('descrição do pedido', max_length=1000)
    data_cadastro = models.DateField('data do cadastro', auto_now_add=True)
    prazo_previsto = models.DateField('prazo previsto')
    status = models.CharField('status', max_length=20, choices=Status.choices, default=Status.EM_ANALISE)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['prazo_previsto', '-data_cadastro']
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'

    def __str__(self):
        return f'Pedido #{self.pk} - {self.cliente.nome}'
