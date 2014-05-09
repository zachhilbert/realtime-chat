from flask import Flask, render_template, request, Response, 
                    redirect, url_for, flash, escape, json
from socketio import socketio_manage
from namespace import SocketNS
from app import app, db
from models import User, Message

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        # If our username is blank, send them back with an error
        if request.form['username'] == '':
            flash('You must submit a nick to enter')
            return render_template('login.html')
        else:
            return redirect(url_for('room'))


@app.route('/room')
def room():
    return render_template('chat.html')


@app.route('/get_messages/<seq_id>')
def get_messages(seq_id):
    new_messages = Message.query.filter(Message.message_id > seq_id).all()
    return simplejson.dumps(build_message_json(new_messages))

@app.route('/socket.io/<path:remaining>')
def socket(remaining):
    try:
        socketio_manage(request.environ, {'/chat': SocketNS}, request)
    except:
        app.logger.error('Socket error', exc_info = True)

    return Response()


def build_message_json(messages):
    r_messages = []
    for message in messages:
        json = dict()
        json['user_id'] = message.user_id
        json['text']    = message.text
        r_messages.append(json)
    
    return {'messages': r_messages}

