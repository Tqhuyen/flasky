from flask_wtf import FLaskForm
from wtforms import StringField, PasswordField

class RegisterForm(FlaskForm):
    username=StringField(label='User Name')
    