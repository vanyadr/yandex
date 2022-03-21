from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField, IntegerField, EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')

    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    age = StringField('Возраст', validators=[DataRequired()])
    position = StringField('Должность', validators=[DataRequired()])
    speciality = StringField('Профессия', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name_p = StringField('Имя пользователя', validators=[DataRequired()])

    submit = SubmitField('Регистрация')


class AddJob(FlaskForm):
    team_leader = IntegerField('Тимлид', validators=[DataRequired()])
    job = StringField('Название работы', validators=[DataRequired()])
    work_size = StringField('Продолжительность', validators=[DataRequired()])
    collaborators = StringField('Участники', validators=[DataRequired()])

    submit = SubmitField('Добавить работу')