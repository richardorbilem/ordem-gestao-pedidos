from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Cliente

class ClienteTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='teste', password='Senha-forte-123')
        self.client.login(username='teste', password='Senha-forte-123')

    def test_cadastro_cliente(self):
        response = self.client.post(reverse('novo_cliente'), {'nome': 'Marina Oliveira', 'telefone': '11999990000', 'email': 'marina@example.com', 'endereco': ''})
        self.assertRedirects(response, reverse('lista_clientes'))
        self.assertTrue(Cliente.objects.filter(nome='Marina Oliveira').exists())

    def test_lista_clientes_exige_login(self):
        self.client.logout()
        response = self.client.get(reverse('lista_clientes'))
        self.assertEqual(response.status_code, 302)
