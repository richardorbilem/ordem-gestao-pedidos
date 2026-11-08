# ORDEM — Gestão de Pedidos para Móveis Planejados

MVP acadêmico desenvolvido como continuidade do protótipo da Experiência Prática II. O objetivo é centralizar clientes e pedidos, permitindo acompanhar descrições, prazos e status.

## Funcionalidades
- Autenticação para proteger as telas internas.
- Cadastro e consulta de clientes.
- Cadastro, consulta, pesquisa e atualização de pedidos.
- Status: Em análise, Em produção, Em instalação, Concluído e Cancelado.
- Painel inicial com atalhos e indicadores.
- Interface responsiva inspirada nas telas do protótipo original.

## Tecnologias
Python 3.12, Django 5.2, SQLite, HTML, CSS e Bootstrap 5.3.

## Executar localmente

```bash
py -3.12 -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Acesse http://127.0.0.1:8000/ e entre com o usuário criado.

## Testes

```bash
python manage.py test
```

O workflow em `.github/workflows/ci.yml` executa os testes automaticamente em push e pull request.

## Observações acadêmicas
Este repositório é um MVP em evolução. Commits, Pull Requests, execuções de CI e validações com representantes devem ser realizados e registrados pelo estudante; não devem ser considerados concluídos apenas por constarem no planejamento. Use somente dados fictícios durante demonstrações.
## Desenvolvimento

Projeto em evolução na branch desenvolvimento.

Nesta etapa serão realizados:
- Implementação do MVP.
- Testes automatizados.
- Revisão de código.
- Integração contínua (CI).

