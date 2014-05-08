from flask import Flask, render_template, request, redirect, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy
#from models import User, Message
import models
import simplejson

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')


# Import db
db = SQLAlchemy(app)

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
            return redirect(url_for('chat'))


@app.route('/chat')
def chat():
    return render_template('chat.html')


@app.route('/get_messages/<seq_id>')
def get_messages(seq_id):
    new_messages = models.Message.query.filter(models.Message.message_id > seq_id).all()
    return simplejson.dumps(build_message_json(new_messages))

def build_message_json(messages):
    r_messages = []
    for message in messages:
        json = dict()
        json['user_id'] = message.user_id
        json['text']    = message.text
        r_messages.append(json)
    
    return {'messages': r_messages}

if __name__ == '__main__':
    app.run()
