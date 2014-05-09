from socketio.namespace import BaseNamespace
from app import app

class SocketNS(BaseNamespace):
    def initialize(self):
        self.logger = app.logger
        self.log('Socket session started')

    def log(self, message):
        self.logger.info('[{0}] {1}'.format(self.socket.sessid, message))

    def recv_connect(self):
        self.log('New connection')

    def recv_disconnect(self):
        self.log('Disconnected')
    
    def on_join(self, name):
        self.log('{0} joined chat'.format(name))
        return True, name
