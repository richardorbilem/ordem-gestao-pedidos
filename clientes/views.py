from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ClienteForm
from .models import Cliente

@login_required
def lista_clientes(request):
    termo = request.GET.get('q', '').strip()
    clientes = Cliente.objects.all()
    if termo:
        clientes = clientes.filter(nome__icontains=termo) | clientes.filter(telefone__icontains=termo)
    return render(request, 'clientes/lista.html', {'clientes': clientes.distinct(), 'termo': termo})

@login_required
def novo_cliente(request):
    form = ClienteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Cliente cadastrado com sucesso.')
        return redirect('lista_clientes')
    return render(request, 'clientes/form.html', {'form': form, 'titulo': 'Novo cliente'})

@login_required
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    form = ClienteForm(request.POST or None, instance=cliente)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Cadastro do cliente atualizado.')
        return redirect('lista_clientes')
    return render(request, 'clientes/form.html', {'form': form, 'titulo': 'Editar cliente'})
