from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateTimeLocalField,EmailField,SelectField
from wtforms.fields.datetime import TimeField
from wtforms.validators import DataRequired, Email

reason = [(1,'Individual Career Counselling'),(2,'Career Protfolio Guidance'),(3,'Resume Advising/Reviews'),
    (4,'Cover Letter Advising Reviews'),(5,'Job Interview Techniques Coaching'),
    (6,'Job Search Assistance'),(7,'Job Referrals-Summer/Part-Time/Full-Time'),(8,'Internship Coordination'),
    (9,'Employment Compensation Package Advising'),(10,'Career Explorations Opportunities'),(11,'Career Development/World of Work Seminars'),
    (12,'Overseas Work & Travel Programme')]

class BookingForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    email = EmailField('Email', [DataRequired()])
    appointment =  SelectField(u'Reason', choices=reason, validate_choice = True, coerce=int)
    date_time = DateTimeLocalField("Date", [DataRequired()], format='%Y-%m-%dT%H:%M')
    submit = SubmitField('Submit')

class RescheduleForm(FlaskForm):
    email = EmailField('Email', [DataRequired()])
    ref_number = StringField('Reference number', [DataRequired()])
    new_date_time = DateTimeLocalField("Date", [DataRequired()], format='%Y-%m-%dT%H:%M')
    submit = SubmitField('Submit')

    