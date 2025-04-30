from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from . import db, login_manager, csrf
from .models import User, Task
from .forms import RegisterForm, LoginForm, TaskForm

main = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main.route('/')
def index():
    return "<h1>Aplicação Flask de Tarefas</h1>"

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    print("⚙️ [DEBUG] register() 👉 método", request.method)
    print("⚙️ [DEBUG] form.errors:", form.errors)
    if form.validate_on_submit():
        print("✅ [DEBUG] validate_on_submit passou! Usuário:", form.username.data)
        hashed_pw = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        flash('Cadastro realizado com sucesso!')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Usuário ou senha incorretos.')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/dashboard')
@login_required
def dashboard():
    return redirect(url_for('main.tasks'))

@main.route('/tasks')
@login_required
def tasks():
    user_tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.date_created.desc()).all()
    return render_template('tasks.html', tasks=user_tasks)

@main.route('/tasks/create', methods=['GET', 'POST'])
@login_required
def create_task():
    form = TaskForm()
    if form.validate_on_submit():
        new_task = Task(title=form.title.data, description=form.description.data, user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
        flash('Tarefa criada com sucesso!')
        return redirect(url_for('main.tasks'))
    return render_template('task_form.html', form=form, action="Criar")

@main.route('/tasks/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        flash('Acesso negado.')
        return redirect(url_for('main.tasks'))
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        db.session.commit()
        flash('Tarefa atualizada com sucesso!')
        return redirect(url_for('main.tasks'))
    return render_template('task_form.html', form=form, action="Editar")

@main.route('/tasks/delete/<int:id>', methods=['POST'])
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    if task.user_id != current_user.id:
        flash('Acesso negado.')
        return redirect(url_for('main.tasks'))
    db.session.delete(task)
    db.session.commit()
    flash('Tarefa deletada com sucesso!')
    return redirect(url_for('main.tasks'))
