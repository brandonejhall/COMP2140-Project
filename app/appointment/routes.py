from flask import Blueprint,render_template,session,redirect
from flask.helpers import url_for



appointment = Blueprint('appoint',__name__,template_folder='templates')

from flask import request
from app.appointment.forms import BookingForm
from app import db
from app.models import Appointments

@appointment.route('/', methods = ['GET','POST'])
def index():
    form = BookingForm()
    if request.method == 'POST':
        name = form.name.data
        dt = str(form.date_time.data)
        app = form.appointment.data
        email = form.email.data
        b = Appointments(name = name,email = email,app_type = app,date_time = dt)
        db.session.add(b)
        db.session.commit()
    return render_template('booking.html',title ='Book Appointment',form = form)

@appointment.route('/page/<data>',methods=['GET'])
def page(data):
    x = str(type(data))
    return x
    
    
