import os

DEBUG = True

# SQLAlchemy
# "db" refers to the name of the db container
SQLALCHEMY_DATABASE_URI = 'postgresql://wmuc:wmuc881@db:5432/wmuc'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# WTForms
WTF_CSRF_ENABLED = True
SECRET_KEY = 'bigbrothersamisalwayswatching'

# Key for itsdangerous
TOKEN_SECRET_KEY = 'wmuc88110watttowerofpower'

# Flask-Mail configuration
# username + password are defined in the app.env file
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

MAIL_SUBJECT_PREFIX = '[WMUC] '
MAIL_SENDER = 'WMUC IT <wmuc.it@gmail.com>'
