from flask_socketio import SocketIO,emit,send
import time
socketio = SocketIO(app, cors_allowed_origins='*')
thread = None
clients = 0
from threading import Thread

#Function that calls the BeagleBone class that is in charged of reading the temperature sensor
def ini_socket():
    global clients, thread
    print("ini socket")
    while clients > 0:
        print('numClientes: {0}'.format(clients))
        #socketio.emit('data-tmp', {'temperature': b.temperature, 'humedity':b.humidity})
        time.sleep(1)
    thread = None #we restore the thread so it can be used again

#Function that runs when a clients get connected to the server
@socketio.on('connect')
def test_connect():
    global clients
    clients += 1
    print('Client connected test')