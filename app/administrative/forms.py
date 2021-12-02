from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateTimeLocalField,EmailField
from wtforms.fields.datetime import DateField, TimeField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    usernumber = StringField('usernumber', [DataRequired()])
    password = StringField('password', [DataRequired()])
    submit = SubmitField('submit')

class EditAvail(FlaskForm):
    weekends = BooleanField('Weekend Appointments')
    start_time = TimeField('Appointment Start Time')
    end_time = TimeField('Appointment End Time')
    special_dates = DateField('No Appointment Day')
    start_date = DateField('Unavailable Dates Start')
    end_date = DateField('Unavailable Dates End')
    submit = SubmitField('submit')





    