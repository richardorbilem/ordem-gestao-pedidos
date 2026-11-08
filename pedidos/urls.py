from django.urls import path
from . import views
urlpatterns = [
    path('', views.painel, name='painel'),
    path('pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('pedidos/novo/', views.novo_pedido, name='novo_pedido'),
    path('pedidos/<int:pk>/editar/', views.editar_pedido, name='editar_pedido'),
]
