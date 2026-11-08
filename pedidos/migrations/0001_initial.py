from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [('clientes', '0001_initial')]
    operations = [migrations.CreateModel(name='Pedido', fields=[
        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('descricao', models.TextField(max_length=1000, verbose_name='descrição do pedido')),
        ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='data do cadastro')),
        ('prazo_previsto', models.DateField(verbose_name='prazo previsto')),
        ('status', models.CharField(choices=[('em_analise', 'Em análise'), ('em_producao', 'Em produção'), ('em_instalacao', 'Em instalação'), ('concluido', 'Concluído'), ('cancelado', 'Cancelado')], default='em_analise', max_length=20, verbose_name='status')),
        ('atualizado_em', models.DateTimeField(auto_now=True)),
        ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pedidos', to='clientes.cliente', verbose_name='cliente')),
    ], options={'verbose_name': 'pedido', 'verbose_name_plural': 'pedidos', 'ordering': ['prazo_previsto', '-data_cadastro']}),]
