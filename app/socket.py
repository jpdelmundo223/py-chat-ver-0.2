from flask_socketio import SocketIO, send, join_room, leave_room
from flask_login import current_user

socketio = SocketIO()

@socketio.on("message")
def handle_message(data):
    message = data["message"]
    room = data["room"]
    print(message + " sent to " + room)
    send(data, broadcast=True, to=room)

@socketio.on("join_room")
def join(data):
    room = data["room"]
    join_room(room)
    print("{username} has joined the room {room}.".format(username=current_user.username, room=room))

@socketio.on("leave_room")
def leave(data):
    room = data["room"]
    leave_room(room)
    print("{username} has left the room {room}.".format(username=current_user.username, room=room))