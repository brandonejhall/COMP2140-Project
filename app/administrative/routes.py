import re
from stat import ST_ATIME
from flask import Blueprint,render_template,session,redirect,flash
from flask_login import current_user, login_user
from flask.helpers import url_for
import string
import random
import datetime
from datetime import date
from operator import itemgetter 

from flask_login.utils import login_required
from app import send_mail
from app import config

admin = Blueprint('administration',__name__,template_folder='templates',static_url_path='/static/administration')

from flask import request
from app.administrative.forms import LoginForm,EditAvail,MockInterviewSetupForm

from app import db
from app.models import AdminUser, Appointments,AvailableTimes, LogStorage, MockInterviewSetup,MockInterviewSignUp



@admin.route('/edit', methods = ['GET','POST'])
@login_required
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


@admin.route('/log', methods= ['GET','POST'])
@login_required
def log():
    log = LogStorage.query.all()
    events = []
    for event in reversed(log):
        events.append(event.logged)
    return render_template('log.html',events = events)

week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
headers = ['DateTime','Day','Name','Reason','reference number']

@admin.route('/generate', methods = ['GET','POST'])
@login_required
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
    
@admin.route('/admini')
@login_required
def admini():
    return render_template('admin.html')


def user_generator(size=6, c=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(c) for _ in range(size))
def pass_generator(size=10, c=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(c) for _ in range(size))


@admin.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if current_user.is_authenticated:
            return redirect(url_for('administration.admini'))
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
            return redirect(url_for('administration.admini'))
    return render_template('login.html', title = 'Sign In', form = form)


@admin.route('/mockinterview', methods = ['GET','POST'])
def mock_setup():
    form = MockInterviewSetupForm()
    if request.method == 'POST':
        s_date = form.start_date.data
        e_date = form.end_date.data
        s_time = form.start_time.data
        e_time = form.end_time.data
        b_time = form.breaktime.data
        interval = form.interval.data
        present = date.today()
        companies = form.companies.data
        if e_date<s_date:
            flash('Mock Interview End Day Error')
        elif s_date<=present or e_date<=present:
            flash('Cannot select present or prior dates')
        elif b_time<s_time or b_time>e_time:
            flash('Break Time needs to be inbetween start and end time')
        elif e_date == None or s_date == None or s_time == None or e_time == None or b_time == None or interval == None:
            flash ("All data needs to be entered")
        else:
            row_count = MockInterviewSetup.query.count()
            if row_count <= 1:
                new_times = MockInterviewSetup(start_date=str(s_date),end_date=str(e_date),start_time=str(s_time),end_time=str(e_time),
                break_time=str(b_time),interval=interval,companies = companies)
                db.session.add(new_times)
                db.session.commit()
                print("DONE!")   
            else:
                setup = MockInterviewSetup.query.first()
                setup.start_date= str(s_date)
                setup.end_date = str(e_date)
                setup.start_time= str(s_time)
                setup.end_time = str(e_time)
                setup.break_time = str(b_time)
                setup.interval = interval
                setup.companies = companies
                print("DONE")
    return render_template('mockinterview_setup.html', title = 'Mock Interview Setup',form = form)

@admin.route('/mocktimetable', methods = ['GET','POST'])
def mock_table():
    MockTable = MockInterviewSignUp.query.all()
    print(type(MockTable[0]))
    print(MockTable[0])
    return render_template('mock_table.html', title = "Mock Interview Timetable")
    
