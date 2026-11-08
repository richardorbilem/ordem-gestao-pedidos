from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [migrations.CreateModel(name='Cliente', fields=[
        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('nome', models.CharField(max_length=120, verbose_name='nome')),
        ('telefone', models.CharField(max_length=20, verbose_name='telefone')),
        ('email', models.EmailField(blank=True, max_length=254, verbose_name='e-mail')),
        ('endereco', models.CharField(blank=True, max_length=255, verbose_name='endereço')),
        ('criado_em', models.DateTimeField(auto_now_add=True)),
    ], options={'verbose_name': 'cliente', 'verbose_name_plural': 'clientes', 'ordering': ['nome']}),]
