from flask import Blueprint,render_template,session,redirect,flash
from flask_login import current_user, login_user
from flask.helpers import url_for
import string
import random
import datetime
from operator import itemgetter 

from flask_login.utils import login_required
from app import send_mail
from app import config

admin = Blueprint('administration',__name__,template_folder='templates',static_url_path='/static/administration')

from flask import request
from app.administrative.forms import LoginForm,EditAvail

from app import db
from app.models import AdminUser, Appointments,AvailableTimes, LogStorage


@login_required
@admin.route('/edit', methods = ['GET','POST'])
def editTimes():
    form = EditAvail()
    if request.method == 'POST':
        weekends = form.weekends.data
        office_hours = str(form.start_time.data)+" "+str(form.end_time.data)
        special = str(form.special_dates.data)
        off_days = str(form.start_date.data) +" "+str(form.end_date.data)
        row_count = AvailableTimes.query.count()
        if row_count < 1:
            new_times = AvailableTimes(weekend=weekends,appointment_hours=office_hours,specific_dates=special,no_appointment=off_days,)
            db.session.add(new_times)
            db.session.commit()
        else:
            times = AvailableTimes.query.first()
            times.weekend = weekends
            times.appointment_hours = office_hours
            times.specific_dates = special
            times.no_appointment = off_days
    return render_template('edit.html', title = 'Edit Times',form = form)

@login_required
@admin.route('/log', methods= ['GET','POST'])
def log():
    log = LogStorage.query.all()
    events = []
    for event in reversed(log):
        events.append(event.logged)
    return render_template('log.html',events = events)

week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
headers = ['DateTime','Day','Name','Reason','reference number']
@login_required
@admin.route('/generate', methods = ['GET','POST'])
def generate():
    #booking = Appointments.query.all()[0].date_time.split()
    #date = booking[0].split('-')
    #time = booking[0].split(':')
    apps = []
    data =  Appointments.query.all()
    for appointments in data:
        date=appointments.date_time.split()[0].split('-')
        time=appointments.date_time.split()[-1].split(':')
        print(time)
        date_time = datetime.datetime(int(date[0]),int(date[1]),int(date[-1]),int(time[0]),int(time[1]))
        
        apps.append([date_time,week[date_time.weekday()],appointments.name,appointments.app_type,appointments.ref_num])
    sorted_lst = sorted(apps,key = lambda x:x[0])
    return render_template('generate.html',sorted_lst = sorted_lst, headers = headers)
    



def user_generator(size=6, c=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(c) for _ in range(size))
def pass_generator(size=10, c=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(c) for _ in range(size))


@admin.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if current_user.is_authenticated:
            return redirect(url_for('administration.admin'))
        user = form.usernumber.data
        passw = form.password.data
        if user == '1001071029':
            password = str(pass_generator())
            username = str(user_generator())
            check= AdminUser.query.filter_by(name = username).first()
            while check is not None:
                username = str(user_generator())
                check = AdminUser.query.filter_by(name = username).first()
            else:
                up =(username,password)
                txt = render_template('email/new_user.txt',userpass = up)
                ht = render_template('email/new_user.html',userpass = up)
                send_mail.send_email('Career Service Admin User',config.Config.MAIL_USERNAME,[config.Config.MAIL_USERNAME],txt,ht)
                new_user=AdminUser(name = username)
                new_user.set_password(password)
                db.session.add(new_user)
                db.session.commit()
                flash (' New User Created','info')
        else:
            check = AdminUser.query.filter_by(name = user).first()
            if check is None or not check.check_password(passw):
                flash('Incorrect Username or Password')
                return redirect(url_for('administration.login'))
            login_user(check)
            return redirect(url_for('administration.admin'))
    return render_template('login.html', title = 'Sign In', form = form)






    
