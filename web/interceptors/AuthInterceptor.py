from application import app
from flask import request
from flask import session
from flask import g
from flask import redirect
from flask import url_for
from common.models.User import User
import re


@app.before_request
def before_request():
    ignore_urls = app.config['IGNORE_URLS']
    ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']
    path = request.path
    pattern = re.compile('|'.join(ignore_check_login_urls))
    if pattern.match(path):
        return
    pattern = re.compile('|'.join(ignore_urls))
    g.current_user = None
    user_info = check_login()
    if user_info:
        g.current_user = user_info
        if pattern.match(path):
            return redirect(url_for('user_page.index'))
    if pattern.match(path):
        return
    if not user_info:
        return redirect(url_for('user_page.login'))
    return


def check_login():
    isLogged = session['isLogged'] if 'isLogged' in session and session['isLogged'] == 1 else None
    if isLogged is None:
        return False
    try:
        user_info = User.query.get(session['id'])
    except:
        return False
    if user_info is None:
        return False
    if user_info.status != 1:
        return False
    return user_info
