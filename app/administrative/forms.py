from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateTimeLocalField,EmailField
from wtforms.fields.datetime import DateField, TimeField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    idnumber = StringField('name', [DataRequired()])
    password = StringField('email', [DataRequired()])
    submit = SubmitField('submit')

class EditAvail(FlaskForm):
    weekends = BooleanField('Check to allow Weekend Appointments')
    start_time = TimeField('Enter what time you would like appointments to start')
    end_time = TimeField('Enter what time you would like bookings to end')
    special_dates = DateField('Enter any date appointments are not allowed')
    start_date = DateField('Enter the start of the range of unavailable dates')
    end_date = DateField('Enter the end of the range of unavailable dates')
    submit = SubmitField('submit')





    