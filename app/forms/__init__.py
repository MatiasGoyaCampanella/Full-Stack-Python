from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired('Este campo es requerido')])
    password = PasswordField('Contraseña', validators=[DataRequired('Este campo es requerido')])
    enviar = SubmitField('Iniciar sesión')


class IngresarContactoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired('Este campo es requerido')])
    apellido = StringField('Apellido', validators=[DataRequired('Este campo es requerido')])
    telefono = StringField('Teléfono', validators=[])
    organismo = StringField('Organismo', validators=[])
    funcion = StringField('Función', validators=[])
    enviar = SubmitField('Agregar nuevo Contacto')
    cancelar = SubmitField('Cancelar', render_kw={'class': 'btn btn-secondary', 'formnovalidate': 'True'})

