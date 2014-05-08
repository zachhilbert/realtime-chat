from app import db

class Message(db.Model):
    __tablename__ = 'messages'

    message_id = db.Column(db.Integer, primary_key = True)
    room_id    = db.Column(db.Integer)
    text       = db.Column(db.Text)
    user_id    = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    datetime   = db.Column(db.DateTime)

    def __repr__(self):
        return '<Message %d - Text:[%r]>' % (self.message_id, self.text)

class User(db.Model):
    __tablename__ = 'users'

    user_id          = db.Column(db.Integer, primary_key = True)
    username         = db.Column(db.String(20))
    datetime_created = db.Column(db.DateTime)

    def __repr__(self):
        return '<User %d: [%r]>' % (self.uesr_id, self.username)

