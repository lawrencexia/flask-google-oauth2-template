import os

basedir = os.path.abspath(os.path.dirname(__file__))

# APP CONFIG
APP_NAME = "Your App Name"
SECRET_KEY = os.environ.get("SECRET_KEY") or "DefaultSecret"
DEBUG = True
WTF_CSRF_ENABLED = True

# GOOGLE OAUTH CONFIG
CLIENT_SECRET_FILE = 'client_secret.json'
G_REDIRECT_URI     = 'https://localhost:5000/gCallback'
G_AUTH_URI         = 'https://accounts.google.com/o/oauth2/auth'
G_TOKEN_URI        = 'https://accounts.google.com/o/oauth2/token'
G_USER_INFO        = 'https://www.googleapis.com/userinfo/v2/me'
G_SCOPE            = 'https://www.googleapis.com/auth/gmail.readonly'