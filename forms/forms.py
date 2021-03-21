from flask_wtf import FlaskForm
from wtforms import DateField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    data1 = DateField('Login', validators=[DataRequired()])
    data2 = DateField('Password', validators=[DataRequired()])