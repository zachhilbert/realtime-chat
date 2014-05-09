from socketio.namespace import BaseNamespace
from socketio.mixins import BroadcastMixin
from app import app, db
from models import User, Message
from flask import escape

class SocketNS(BaseNamespace, BroadcastMixin):
    def initialize(self):
        self.logger = app.logger
        self.log('Socket session started')

    def log(self, message):
        self.logger.info('[{0}] {1}'.format(self.socket.sessid, message))
    
    def on_join(self, name):
        # clean and truncate name
        nick = escape( name[:20] if len(name) > 20 else name )
        self.log('{0} joined chat'.format(nick))
        self.session['username'] = nick
        user = User.query.filter_by(username=nick)
        if user == None:
            user = User(nick)
            db.session.add(user)
            db.session.commit()

        return True, nick

    def on_message(self, message):
        self.log('got message {0} from >{1}<'.format(message, self.session['username']))
        # create and persist message
        message_obj = Message(message, self.session['username'])
        db.session.add(message_obj)
        db.session.commit()

        self.broadcast_event_not_me('message', {
            'sender': self.session['username'],
            'text': message})
        return True, message

