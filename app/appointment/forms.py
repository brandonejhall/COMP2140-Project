from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateTimeLocalField,EmailField
from wtforms.fields.datetime import TimeField
from wtforms.validators import DataRequired, Email


class BookingForm(FlaskForm):
    name = StringField('name', [DataRequired()])
    email = EmailField('email', [DataRequired()])
    appointment =  StringField('booking', [DataRequired()])
    date_time = DateTimeLocalField("Date (DD-MM-YYYY)", [DataRequired()], format='%Y-%m-%dT%H:%M')
    submit = SubmitField('submit')
    