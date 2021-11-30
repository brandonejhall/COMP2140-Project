from flask import Blueprint,render_template,session,redirect,flash
from flask.helpers import url_for
import string
import random
from app import send_mail
from app import config

admin = Blueprint('administration',__name__,template_folder='templates')

from flask import request
from app.administrative.forms import LoginForm,EditAvail

from app import db
from app.models import AdminUser



@admin.route('/edit', methods = ['GET','POST'])
def editTimes():
    form = EditAvail()
    if request.method == 'POST':
        weekends = form.weekends.data
        office_hours = str(form.start_time.data)+" "+str(form.end_time.data)
        special = str(form.special_dates.data)
        off_days = str(form.start_date.data) + str(form.end_date.data)
    return render_template('edit.html', title = 'Edit Times',form = form)

@admin.route('/login', methods = ['GET','POST'])
def login():
    pass



    
