from flask import Blueprint,render_template

appointment = Blueprint('appoint',__name__)


@appointment.route('/', methods = ['GET','POST'])
def index():
    return '<h1>Hello World</h1>'