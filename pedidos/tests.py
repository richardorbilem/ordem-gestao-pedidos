from datetime import date, timedelta
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from clientes.models import Cliente
from .models import Pedido

class PedidoTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='teste', password='Senha-forte-123')
        self.client.login(username='teste', password='Senha-forte-123')
        self.cliente = Cliente.objects.create(nome='Marina Oliveira', telefone='11999990000')

    def test_criar_pedido(self):
        response = self.client.post(reverse('novo_pedido'), {
            'cliente': self.cliente.pk,
            'descricao': 'Armário planejado para cozinha',
            'prazo_previsto': (date.today() + timedelta(days=30)).isoformat(),
            'status': Pedido.Status.EM_ANALISE,
        })
        self.assertRedirects(response, reverse('lista_pedidos'))
        self.assertEqual(Pedido.objects.count(), 1)
        self.assertEqual(Pedido.objects.first().cliente, self.cliente)

    def test_atualizar_status_pedido(self):
        pedido = Pedido.objects.create(cliente=self.cliente, descricao='Painel para sala', prazo_previsto=date.today() + timedelta(days=20))
        response = self.client.post(reverse('editar_pedido', args=[pedido.pk]), {
            'cliente': self.cliente.pk, 'descricao': pedido.descricao,
            'prazo_previsto': pedido.prazo_previsto.isoformat(), 'status': Pedido.Status.EM_PRODUCAO,
        })
        self.assertRedirects(response, reverse('lista_pedidos'))
        pedido.refresh_from_db()
        self.assertEqual(pedido.status, Pedido.Status.EM_PRODUCAO)

    def test_consulta_pedidos(self):
        Pedido.objects.create(cliente=self.cliente, descricao='Armário cozinha', prazo_previsto=date.today() + timedelta(days=10))
        response = self.client.get(reverse('lista_pedidos'), {'q': 'Marina'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Armário cozinha')
