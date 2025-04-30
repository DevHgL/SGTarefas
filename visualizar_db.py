import os
from app import create_app, db
from app.models import User, Task

# 1) Inicializa a app e o contexto
app = create_app()
app.app_context().push()

# 2) Garante que as tabelas existem (cria se não existirem)
db.create_all()

# 3) Informa onde está o arquivo SQLite e seu tamanho
db_path = os.path.abspath("tasks.db")
size = os.path.getsize(db_path) if os.path.exists(db_path) else 0
print(f"📁 Arquivo de banco: {db_path} ({size} bytes)")

# 4) Lê e exibe os registros
print("\n📋 Usuários cadastrados:")
users = User.query.all()
if users:
    for u in users:
        print(f" • ID={u.id} | usuário='{u.username}'")
else:
    print(" (nenhum usuário)")

print("\n🗂 Tarefas cadastradas:")
tasks = Task.query.all()
if tasks:
    for t in tasks:
        print(f" • ID={t.id} | título='{t.title}' | usuário_id={t.user_id}")
else:
    print(" (nenhuma tarefa)")
