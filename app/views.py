import httplib2
from functools import wraps

from flask import render_template, jsonify, redirect, url_for, session, request
from apiclient import discovery, errors
from oauth2client import client

from app import app


def login_required(route):
    @wraps(route)
    def redirect_if_no_credentials(*args, **kwargs):
        if 'credentials' not in session:
            session['redirect_url'] = request.url
            return redirect(url_for('oauth2callback'))
        credentials = client.OAuth2Credentials.from_json(session['credentials'])
        if credentials.access_token_expired:
            session['redirect_url'] = request.url
            return redirect(url_for('oauth2callback'))
        return route(*args, **kwargs)

    return redirect_if_no_credentials


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
@login_required
def profile():
    credentials = client.OAuth2Credentials.from_json(session['credentials'])
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    """
    Doc on what to call with gmail service:
        https://developers.google.com/resources/api-libraries/documentation/gmail/v1/python/latest/
    """
    profile = service.users().getProfile(userId='me').execute()

    return jsonify(profile)


@app.route('/gCallback')
def oauth2callback():
    flow = client.flow_from_clientsecrets(app.config.get('CLIENT_SECRET_FILE'),
                                          scope=app.config.get('G_SCOPE'),
                                          redirect_uri=url_for('oauth2callback', _external=True))
    flow.user_agent = app.config.get('APP_NAME')
    if 'code' not in request.args:
        auth_url = flow.step1_get_authorize_url()
        return redirect(auth_url)
    else:
        auth_code = request.args.get('code')
        credentials = flow.step2_exchange(auth_code)
        session['credentials'] = credentials.to_json()

        if session.get('redirect_url'):
            redirect_url = session.get('redirect_url')
            del session['redirect_url']
            return redirect(redirect_url)

        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    if 'credentials' in session:
        credentials = client.OAuth2Credentials.from_json(session.get('credentials'))
        if credentials:
            http = credentials.authorize(httplib2.Http())
            credentials.revoke(http)
    session.clear()
    return redirect(url_for('index'))
