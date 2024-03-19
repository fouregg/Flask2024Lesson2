from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class SimpleForm(FlaskForm):
    username = StringField("Введите имя пользователя")

    '''
    password = PasswordField("Введите пароль")
    float_test = FloatField("Введите дробное число")
    integer_test = IntegerField("Введите целочисленное")
    password_test = PasswordField("Введите пароль")
    radio_test = RadioField("Поставьте галочку")
    select_test = SelectField("Выберите из списка", choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    text_test = TextAreaField("Введите текст:")
    '''
    submit = SubmitField("Авторизоваться!")