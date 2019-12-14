from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateTimeLocalField,DateTimeField
from datetime import datetime

class RemindForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    source = StringField('source', validators=[DataRequired()])
    destination = StringField('destination', validators=[DataRequired()])
    time = StringField('time', validators=[DataRequired()])
    submit = SubmitField('remind')