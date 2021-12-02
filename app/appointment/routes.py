from flask import Blueprint,render_template,session,redirect,flash
from flask.helpers import url_for
import string
import random
import datetime
from app import send_mail
from app import config


appointment = Blueprint('appoint',__name__,template_folder='templates',static_folder='static', static_url_path='/static/appoint')

from flask import request
from app.appointment.forms import BookingForm, RescheduleForm, reason
from app import db
from app.models import Appointments,AvailableTimes, LogStorage

def id_generator(size=12, c=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(c) for _ in range(size))

def date_check(dt):
    dt_check = dt.split()[0].split('-')
    date_time = datetime.date(int(dt_check[0]),int(dt_check[1]),int(dt_check[2]))
    check = AvailableTimes.query.first()
    range = check.no_appointment.split()
    weekend = check.weekend
    earliest_day=datetime.date.today() + datetime.timedelta(days=1)
    # checks if date ranges were set and capture the ranges in which appointments cannot be set
    if range[0] != 'None':
        start = datetime.date(int(range[0].split('-')[0]),int(range[0].split('-')[1]),int(range[0].split('-')[2]))
        start_exists = True
    else:
        start_exists = False
    if range[1] != 'None':
        end = datetime.date(int(range[1].split('-')[0]),int(range[1].split('-')[1]),int(range[1].split('-')[2]))
        end_exists = True
    else:
        end_exists = False
        
    #checks if any specific date exists to take into consideration for booking
    if (check.specific_dates != 'None'):
        s_date = datetime.date(int(check.specific_dates.split('-')[0]),int(check.specific_dates.split('-')[1]),int(check.specific_dates.split('-')[2]))
        s_date_real = True
    else:
        s_date_real = False   

    if start_exists and end_exists:
        if (start<=date_time<=end):
            flash("Please enter a date which is not in the range "+ range[0] + " - " + range[1],"error")
            range_ok = False
        else:
            range_ok = True
    else:
        range_ok =True

    if s_date_real:
        if s_date == date_time:
            spec_ok = False
            flash("Please enter a date which is not this specific day "+ check.specific_dates,"error")
        else:
            spec_ok = True
    else:
        spec_ok = True
    if earliest_day>date_time:
        e_day=False
    else:
        e_day = True

    if (not weekend):
        if date_time.weekday()>4:
            flash('No Weekend Appointments are allowed','error')
            w_end = False
        else:
            w_end = True

    return [spec_ok,range_ok,e_day,w_end]

def time_check(dt):
    time=dt.split()[-1].split(':')
    time_range =  AvailableTimes.query.first().appointment_hours.split()
    start = int(time_range[0].split(':')[0])
    end = int(time_range[1].split(':')[0])
    if (int(time[1])== 0 or int(time[1])== 30):
        time_ok = True
    else:
        flash('Time should be at the start or the middle of an hour','error') 
        time_ok = False 

    if start<int(time[0])<end:
        t_range = True
    else:
        flash('Enter a time between 9am and 4pm','error')
        t_range = False
    return [time_ok,t_range] 

def database_check(dt):
    if (Appointments.query.filter_by(date_time = dt).first() is None):
        unbooked = True
    else:
        unbooked = False
    return unbooked

@appointment.route('/', methods = ['GET','POST'])
def index():
    form = BookingForm()
    if request.method == 'POST':

        name = form.name.data
        dt = str(form.date_time.data)
        d_check =  date_check(dt)
        t_check = time_check(dt)
        db_check = database_check(dt)
        app = dict(reason)[form.appointment.data]
        email = form.email.data
        test_ref_num = id_generator()
        
        #checks if reference number is already in database
        while (Appointments.query.filter_by(ref_num=test_ref_num).first() is not None):
            test_ref_num = id_generator()    
        else:
            #checks if dates entered are valid
            if (d_check[0] and d_check[1] and d_check[2] and d_check[3] and t_check[0] and t_check[1] and db_check ):
                log = LogStorage (logged = f"{name} booked an appointment for {app} at {dt}")
                booking = Appointments(ref_num = test_ref_num,name = name,email = email,app_type = app,date_time = dt)
                txt = render_template('emails_notifs/book.txt',booking = booking)
                ht = render_template('emails_notifs/book.html',booking = booking)
                send_mail.send_email('Career Service Appointment',config.Config.MAIL_USERNAME,[email],txt,ht)
                flash('Confirmation email sent','info')
            
                db.session.add(booking)
                db.session.add(log)
                db.session.commit()

    return render_template('homepage.html',title ='Book Appointment',form = form)
    #remember to check if user has appointment already with the same reason flash "Appointment already exists please visit reschedule section"



@appointment.route('/reschedule',methods=['GET','POST'])
def reschedule():
    form = RescheduleForm()
    if request.method == 'POST':
        email = form.email.data
        ref_num = form.ref_number.data
        dt = str(form.new_date_time.data)
        d_check =  date_check(dt)
        t_check = time_check(dt)
        db_check = database_check(dt)
        app = Appointments.query.filter_by(ref_num=ref_num).first()
        if (app is None):
            flash ('No appointment exists with the given reference number','error')
        if app.email == email:
            if (d_check[0] and d_check[1] and d_check[2] and d_check[3] and t_check[0] and t_check[1] and db_check ):
                log = LogStorage (logged = f"{app.name} rescheduled an appointment for {app.date_time} to {dt}")
                app.date_time = dt
                db.session.add(log)
                db.session.commit()
    return render_template('reschedule.html',title ='Reschedule Appointment',form = form)
    
