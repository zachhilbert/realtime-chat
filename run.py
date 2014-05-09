from gevent import monkey
from socketio.server import SocketIOServer
from app import app, db
from models import *
from views import *

monkey.patch_all()

if __name__ == '__main__':
    SocketIOServer(
            ('', app.config['SOCKET_IO_PORT']),
            app, resource='socket.io').serve_forever()
