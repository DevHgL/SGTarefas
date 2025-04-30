Sistemas de Gerenciamento de Tarefas

Este projeto é um sistema de gerenciamento de tarefas simples construído com Flask, Flask-SQLAlchemy, Flask-Login e Flask-WTF, utilizando SQLite como banco de dados e Bootstrap 5 para a interface.

🗂️ Funcionalidades

Registro e autenticação de usuários (Flask-Login)

CRUD completo de tarefas (criar, listar, editar, excluir)

Proteção CSRF em formulários (Flask-WTF)

Páginas renderizadas com Jinja2 e Bootstrap 5

Banco de dados SQLite local (tasks.db)

🚀 Tecnologias

Python 3.x

Flask

Flask-SQLAlchemy

Flask-Login

Flask-WTF

Jinja2

SQLite

Bootstrap 5 (CDN)

📁 Estrutura do Projeto

task_manager/
├── app/
│   ├── __init__.py        # Inicialização da aplicação e configuração
│   ├── models.py          # Modelos SQLAlchemy: User e Task
│   ├── forms.py           # Formulários WTForms
│   ├── routes.py          # Blueprints e rotas
│   └── templates/         # Templates HTML (Bootstrap)
│       ├── base.html
│       ├── login.html
│       ├── register.html
│       ├── dashboard.html
│       ├── tasks.html
│       └── task_form.html
├── run.py                 # Script principal para rodar o servidor
├── visualizar_db.py       # Script de depuração e visualização do banco
├── requirements.txt       # Dependências do projeto
└── tasks.db               # Banco de dados SQLite (gerado após primeira execução)

⚙️ Como rodar localmente

Clone o repositório

git clone <URL_DO_REPO>
cd task_manager

Crie e ative um ambiente virtual

python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate      # Windows

Instale as dependências

pip install -r requirements.txt

Inicialize o banco de dadosNa primeira execução, crie as tabelas manualmente executando no Python shell:

python
>>> from app import create_app, db
>>> app = create_app()
>>> app.app_context().push()
>>> db.create_all()
>>> exit()

Execute a aplicação

python run.py

Acesse http://127.0.0.1:5000 no navegador.

🎯 Uso

Registrar um novo usuário:Acesse /register, preencha usuário e senha.

Login:Acesse /login, entre com suas credenciais.

Gerenciar Tarefas:

GET /tasks — lista de tarefas do usuário.

GET /tasks/create — formulário para criar nova tarefa.

GET /tasks/edit/<id> — editar tarefa existente.

POST /tasks/delete/<id> — excluir tarefa.

📜 Licença

Este projeto está licenciado sob a MIT License.

🤝 Contribuição

Fork este repositório.

Crie uma branch para sua feature: git checkout -b feature/nova-funcionalidade

Commit suas mudanças: git commit -m 'Adiciona nova funcionalidade'

Push para a branch: git push origin feature/nova-funcionalidade

Abra um Pull Request.

Desenvolvido por Hugo Leonardo Melo — GitHub | LinkedIn

