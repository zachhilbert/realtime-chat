from app import db
import datetime

class User(db.Model):
    __tablename__ = 'users'

    def __init__(self, username):
        self.username = username

    user_id          = db.Column(db.Integer, primary_key = True)
    username         = db.Column(db.String(20))
    datetime_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<User %d: [%r]>' % (self.uesr_id, self.username)


class Message(db.Model):
    __tablename__ = 'messages'

    def __init__(self, text, username):
        self.text = text
        user = User.query.filter_by(username=username).first()
        if user == None:
            user = User(username)
        self.user_id = user.user_id


    message_id = db.Column(db.Integer, primary_key = True)
    text       = db.Column(db.Text)
    user_id    = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    datetime   = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return '<Message %d - Text:[%r]>' % (self.message_id, self.text)


def build_message_json(messages):
    r_messages = []
    for message in messages:
        json = dict()
        user = User.query.filter_by(user_id=message.user_id).first()
        json['sender'] = user.username if user != None else 'Missing'
        json['text']    = message.text
        r_messages.append(json)
    
    return {'messages': r_messages}

