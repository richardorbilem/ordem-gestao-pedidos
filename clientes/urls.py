from django.urls import path
from . import views
urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('novo/', views.novo_cliente, name='novo_cliente'),
    path('<int:pk>/editar/', views.editar_cliente, name='editar_cliente'),
]
