from gevent import monkey
monkey.patch_all()

import time
from threading import Thread
from flask import Flask, render_template, session, request,jsonify,request
from flask.ext.socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

nbstring = ""


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('my connect', namespace='/test')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my connect', {'data': message['data'], 'count': session['receive_count']})



@socketio.on('my log', namespace='/test')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my change', {'data': message['data']}, broadcast=True)



if __name__ == '__main__':
    socketio.run(app)
