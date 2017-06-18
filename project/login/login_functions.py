from manage import User
from flask import redirect, url_for, session
import logging
from flask_server import db


def is_valid(name, login):

    user = User.query.filter_by(user_name=name).one()

    logging.warn(user.password)
    logging.warn(login)
    logging.warn(user.password == user.password)
    logging.warn(user.password == login)

    if user:
        if user.password == login:
            logging.warn("login succussful")
            return True
        else:
            logging.warn(user.password == user.password)
            logging.warn(user.password == login)
            logging.warn("id does not equal code")
            return False
    else:
        logging.warn("user does not exsist")
        return False


def login_needed():
    try:
        if session.user:
            return
        else:
            return redirect(url_for('login'))
    except:
        return redirect(url_for('login'))