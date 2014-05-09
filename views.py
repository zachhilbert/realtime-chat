from flask import Flask, render_template, request, Response, \
        redirect, url_for, flash, escape, json, \
        session
from socketio import socketio_manage
from namespace import SocketNS
from app import app, db
from models import User, Message, build_message_json
import datetime


"""
Base route for login page
"""
@app.route('/')
def index():
    return render_template('login.html')


@app.route('/get_messages')
def get_messages():
    max_message_timeframe = datetime.datetime.now() - datetime.timedelta(minutes=10)
    new_messages = Message.query.filter(Message.datetime > max_message_timeframe).all()
    return json.dumps(build_message_json(new_messages))

"""
Socket io address
"""
@app.route('/socket.io/<path:remaining>')
def socket(remaining):
    try:
        socketio_manage(request.environ, {'/chat': SocketNS}, request)
    except:
        app.logger.error('Socket error', exc_info = True)

    return Response()


