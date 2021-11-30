from flask import Blueprint,render_template,session,redirect,flash
from flask.helpers import url_for
import string
import random
import datetime
from app import send_mail
from app import config


appointment = Blueprint('appoint',__name__,template_folder='templates')

from flask import request
from app.appointment.forms import BookingForm, RescheduleForm
from app import db
from app.models import Appointments,AvailableTimes

def id_generator(size=12, c=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(c) for _ in range(size))

def date_check(dt):
    dt_check = dt.split()[0].split('-')
    date_time = datetime.datetime(int(dt_check[0]),int(dt_check[1]),int(dt_check[2]))
    check = AvailableTimes.query.first()
    range = check.no_appointment.split()
    # checks if date ranges were set and capture the ranges in which appointments cannot be set
    if range[0] != 'None':
        start = datetime.datetime(int(range[0].split('-')[0]),int(range[0].split('-')[1]),int(range[0].split('-')[1]))
        start_exists = True
    else:
        start_exists = False
    if range[1] != 'None':
        end = datetime.datetime(int(range[1].split('-')[0]),int(range[1].split('-')[1]),int(range[1].split('-')[1]))
        end_exists = True
    else:
        end_exists = False
        
    #checks if any specific date exists to take into consideration for booking
    if (check.specific_dates != 'None'):
        s_date = datetime.datetime(int(check.specific_dates.split('-')[0]),int(check.specific_dates.split('-')[1]),int(check.specific_dates.split('-')[2]))
        s_date_real = True
    else:
        s_date_real = False   

    if start_exists and end_exists:
        if (start<=date_time<=end):
            flash("Please enter a date which is not in the range "+ range[0].split('-') + " - " + range[1].split('-'),"error")
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
    return [spec_ok,range_ok]


@appointment.route('/book', methods = ['GET','POST'])
def index():
    form = BookingForm()
    if request.method == 'POST':

        name = form.name.data
        dt = str(form.date_time.data)
        check =  date_check(dt)
        app = form.appointment.data
        email = form.email.data
        test_ref_num = id_generator()
        #checks if reference number is already in database
        while (Appointments.query.filter_by(ref_num=test_ref_num).first() is not None):
            test_ref_num = id_generator()    
        else:
            #checks if dates entered are valid
            if (check[0] and check[1]):
                booking = Appointments(ref_num = test_ref_num,name = name,email = email,app_type = app,date_time = dt)
                txt = render_template('emails_notifs/book.txt',booking = booking)
                ht = render_template('emails_notifs/book.html',booking = booking)
                send_mail.send_email('Career Service Appointment',config.Config.MAIL_USERNAME,[email],txt,ht)
            
                db.session.add(booking)
                db.session.commit()

    return render_template('booking.html',title ='Book Appointment',form = form)
    #remember to check if user has appointment already with the same reason flash "Appointment already exists please visit reschedule section"

@appointment.route('/reschedule',methods=['GET','POST'])
def reschedule():
    form = RescheduleForm()
    if request.method == 'POST':
        email = form.email.data
        ref_num = form.ref_number.data
        dt = str(form.new_date_time.data)
        app = Appointments.query.filter_by(ref_num=ref_num).first()
        if (app is None):
            pass
        if app.email == email:
            app.date_time = dt
            db.session.commit()
    return render_template('reschedule.html',title ='Reschedule Appointment',form = form)
    
