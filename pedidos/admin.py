from django.contrib import admin
from .models import Pedido
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'prazo_previsto', 'status', 'data_cadastro')
    list_filter = ('status', 'prazo_previsto')
    search_fields = ('cliente__nome', 'descricao')
