from wtforms.fields.datetime import DateField
from app import db,login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin

class AdminUser(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(45),index= True)
    password = db.Column(db.String(128))


    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password,password)


@login.user_loader
def load_user(id):
    return AdminUser.query.get(int(id))


class Appointments(db.Model):
    ref_id = db.Column(db.Integer,primary_key = True)
    ref_num = db.Column(db.String(12),index=True)
    name = db.Column(db.String(45),index = True)
    email = db.Column(db.String(45),index = True)
    app_type = db.Column(db.String(45),index = True)
    date_time = db.Column(db.String(),index = True)


class AvailableTimes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    weekend = db.Column(db.Boolean, default=False, nullable=False)
    appointment_hours = db.Column(db.String(), default ='')
    specific_dates = db.Column(db.String(), default = '')
    no_appointment = db.Column(db.String(), default = '') 


class LogStorage(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    logged = db.Column(db.String(), index =True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now())

class MockInterviewSetup(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    start_date = db.Column(db.String(), index = True)
    end_date = db.Column(db.String(), index = True)
    start_time = db.Column(db.String(), index = True)
    end_time = db.Column(db.String(), index = True)
    break_time = db.Column(db.String(), index =True)
    interval = db.Column(db.Integer, index = True)
    companies = db.Column(db.String(), index = True)

class MockInterviewSignUp(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), index = True)
    major = db.Column(db.String(), index = True)
    date = db.Column(db.String(), index = True)
    time = db.Column(db.String(), index = True)
    company = db.Column(db.String(), index = True)




def __repr__(self):
    return '<Appointments {}>'.format(self.name)

def init_db():
    db.create_all()

if __name__ == '__main__':
    init_db()