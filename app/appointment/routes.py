from flask import Blueprint,render_template,session,redirect,flash
from flask.helpers import url_for
import string
import random
from app import send_mail
from app import config


appointment = Blueprint('appoint',__name__,template_folder='templates')

from flask import request
from app.appointment.forms import BookingForm, RescheduleForm
from app import db
from app.models import Appointments

def id_generator(size=12, c=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(c) for _ in range(size))

@appointment.route('/book', methods = ['GET','POST'])
def index():
    form = BookingForm()
    if request.method == 'POST':
        name = form.name.data
        dt = str(form.date_time.data)
        app = form.appointment.data
        email = form.email.data
        test_ref_num = id_generator()
        while (Appointments.query.filter_by(ref_num=test_ref_num).first() is not None):
            test_ref_num = id_generator()    
        else:
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
    
