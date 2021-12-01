import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #SECRET KEY CONFIGURATION
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    #SQLALCHMEY CONFIGURATION
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #MAIL SERVER CONFIGURATION
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 1
    MAIL_USERNAME = 'careerservicesbooking@gmail.com'
    MAIL_PASSWORD = 'comp2140'

    #PAGINATION
    LOG_PER_PAGE = 5
