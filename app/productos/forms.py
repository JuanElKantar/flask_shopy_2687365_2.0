from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField

class NewProductForm(FlaskForm):
    nameproduct = StringField('ingrese el precio')
    precio = SubmitField('ingrese precio')
    submit = SubmitField("registrar")