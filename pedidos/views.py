from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import PedidoForm
from .models import Pedido

@login_required
def painel(request):
    pedidos = Pedido.objects.select_related('cliente')
    recentes = pedidos[:5]
    contexto = {
        'total_pedidos': pedidos.count(),
        'em_andamento': pedidos.exclude(status__in=[Pedido.Status.CONCLUIDO, Pedido.Status.CANCELADO]).count(),
        'concluidos': pedidos.filter(status=Pedido.Status.CONCLUIDO).count(),
        'atrasados': pedidos.filter(prazo_previsto__lt=timezone.localdate()).exclude(status__in=[Pedido.Status.CONCLUIDO, Pedido.Status.CANCELADO]).count(),
        'recentes': recentes,
    }
    return render(request, 'pedidos/painel.html', contexto)

@login_required
def lista_pedidos(request):
    termo = request.GET.get('q', '').strip()
    status = request.GET.get('status', '').strip()
    pedidos = Pedido.objects.select_related('cliente')
    if termo:
        criterio = Q(cliente__nome__icontains=termo) | Q(descricao__icontains=termo)
        if termo.isdigit():
            criterio |= Q(pk=int(termo))
        pedidos = pedidos.filter(criterio)
    if status in Pedido.Status.values:
        pedidos = pedidos.filter(status=status)
    return render(request, 'pedidos/lista.html', {'pedidos': pedidos, 'termo': termo, 'status_atual': status, 'status_opcoes': Pedido.Status.choices})

@login_required
def novo_pedido(request):
    form = PedidoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        pedido = form.save()
        messages.success(request, f'Pedido #{pedido.pk} cadastrado com sucesso.')
        return redirect('lista_pedidos')
    return render(request, 'pedidos/form.html', {'form': form, 'titulo': 'Novo pedido'})

@login_required
def editar_pedido(request, pk):
    pedido = get_object_or_404(Pedido.objects.select_related('cliente'), pk=pk)
    form = PedidoForm(request.POST or None, instance=pedido)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f'Pedido #{pedido.pk} atualizado com sucesso.')
        return redirect('lista_pedidos')
    return render(request, 'pedidos/form.html', {'form': form, 'titulo': f'Editar pedido #{pedido.pk}', 'pedido': pedido})
