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


<<<<<<< HEAD
class MockInterviewSetupForm(FlaskForm):
    start_date = DateField('Start Date: ',[DataRequired()],format='%Y-%m-%d')
    end_date = DateField('End Date: ',[DataRequired()],format='%Y-%m-%d')
    start_time = TimeField('StartTime(HH:MM)',[DataRequired()])
    end_time = TimeField('EndTime(HH:MM)',[DataRequired()])
    interval = IntegerField('Interview Intervals(in minutes)',[DataRequired()])
    breaktime = TimeField('BreakTime(HH:MM)',[DataRequired()])
    extrabreak = TimeField('Extra Break(HH:MM)',[DataRequired()])
    companies = StringField('Companies', [DataRequired()])
    submit = SubmitField('submit')
=======
>>>>>>> 39d67735078fc115c5081bf3026c19db1f37939d



    