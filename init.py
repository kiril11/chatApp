from flask import Flask
from flask_socketio import SocketIO, send
import bcrypt

app = Flask(__name__)

socketio = SocketIO(app)
from views import *
from events import *

app.config['SECRET_KEY'] = '1221'


if __name__ == '__main__':
    socketio.run(app)