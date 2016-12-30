import os

basedir = os.path.abspath(os.path.dirname(__file__))

# APP CONFIG
APP_NAME = "Your App Name"
SECRET_KEY = os.environ.get("SECRET_KEY") or "DefaultSecret"
DEBUG = True
WTF_CSRF_ENABLED = True

# GOOGLE OAUTH CONFIG
CLIENT_SECRET_FILE = 'client_secret.json'
G_SCOPE            = 'https://www.googleapis.com/auth/gmail.readonly'