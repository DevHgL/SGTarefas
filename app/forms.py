from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length

class RegisterForm(FlaskForm):
    username = StringField('Usuário', validators=[InputRequired(), Length(min=4, max=150)])
    password = PasswordField('Senha', validators=[InputRequired(), Length(min=4, max=150)])
    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[InputRequired(), Length(min=4, max=150)])
    password = PasswordField('Senha', validators=[InputRequired(), Length(min=4, max=150)])
    submit = SubmitField('Entrar')

class TaskForm(FlaskForm):
    title = StringField('Título', validators=[InputRequired(), Length(min=1, max=200)])
    description = TextAreaField('Descrição')
    submit = SubmitField('Salvar')
