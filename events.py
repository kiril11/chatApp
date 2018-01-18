from init import *
from flask_socketio import send
from flask import session



@socketio.on('message')
def handle_message(msg):
    user = session.get('user')
    msg = user + ": " + msg
    send(msg, broadcast=True)
