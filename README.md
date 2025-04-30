# Task Manager Flask Application

Este projeto é um sistema de gerenciamento de tarefas simples construído com **Flask**, **Flask-SQLAlchemy**, **Flask-Login** e **Flask-WTF**, utilizando **SQLite** como banco de dados e **Bootstrap 5** para a interface.

---

## 🗂️ Funcionalidades

- Registro e autenticação de usuários (Flask-Login)
- CRUD completo de tarefas (criar, listar, editar, excluir)
- Proteção CSRF em formulários (Flask-WTF)
- Páginas renderizadas com Jinja2 e Bootstrap 5
- Banco de dados SQLite local (`tasks.db`)

---

## 🚀 Tecnologias

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF
- Jinja2
- SQLite
- Bootstrap 5 (CDN)

---

## 📁 Estrutura do Projeto

```
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
```

---

## ⚙️ Como rodar localmente

1. **Clone o repositório**  
   ```bash
   git clone <URL_DO_REPO>
   cd task_manager
   ```

2. **Crie e ative um ambiente virtual**  
   ```bash
   python -m venv venv
   source venv/bin/activate     # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Instale as dependências**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicialize o banco de dados**  
   Na primeira execução, crie as tabelas manualmente executando no Python shell:
   ```bash
   python
   >>> from app import create_app, db
   >>> app = create_app()
   >>> app.app_context().push()
   >>> db.create_all()
   >>> exit()
   ```

5. **Execute a aplicação**  
   ```bash
   python run.py
   ```
   Acesse `http://127.0.0.1:5000` no navegador.

---

## 🎯 Uso

1. **Registrar** um novo usuário:  
   Acesse `/register`, preencha usuário e senha.

2. **Login**:  
   Acesse `/login`, entre com suas credenciais.

3. **Gerenciar Tarefas**:  
   - `GET /tasks` — lista de tarefas do usuário.
   - `GET /tasks/create` — formulário para criar nova tarefa.
   - `GET /tasks/edit/<id>` — editar tarefa existente.
   - `POST /tasks/delete/<id>` — excluir tarefa.

---


## 🤝 Contribuição

1. Fork este repositório.  
2. Crie uma branch para sua feature: `git checkout -b feature/nova-funcionalidade`  
3. Commit suas mudanças: `git commit -m 'Adiciona nova funcionalidade'`  
4. Push para a branch: `git push origin feature/nova-funcionalidade`  
5. Abra um Pull Request.

---

> Desenvolvido por Hugo Leonardo Melo — [GitHub](https://github.com/DevHgL) | [LinkedIn](https://www.linkedin.com/in/hugolmelo/)

