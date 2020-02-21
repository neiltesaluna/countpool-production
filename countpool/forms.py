from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField

class NewTimer(FlaskForm):

    title = StringField('Timer', validators=[DataRequired(), Length(min=2, max=20)])

    date = DateField('Date', validators=[DataRequired()])

    submit = SubmitField('New Timer')
