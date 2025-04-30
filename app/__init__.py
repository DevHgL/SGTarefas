from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'chave_secreta_segura'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['WTF_CSRF_ENABLED'] = False

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
