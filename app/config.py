import os
from datetime import timedelta, datetime

basedir = os.path.abspath(os.path.dirname(__file__))

print(basedir)

DEBUG = True
WTF_CSRF_ENABLED = True
SECRET_KEY = "46c0838a8c3146a3c6b5af2bac9381bd233978a2388f1aaf35937b32d3c06271"
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "db.sqlite")
SQLALCHEMY_TRACK_MODIFICATIONS = False
REMEMBER_COOKIE_DURATION = timedelta(seconds=20)
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = "465"
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
MAIL_USE_TLS = False
MAIL_USE_SSL = True