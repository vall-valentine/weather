from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    data1 = StringField('Login', validators=[DataRequired()])
    data2 = StringField('Password', validators=[DataRequired()])