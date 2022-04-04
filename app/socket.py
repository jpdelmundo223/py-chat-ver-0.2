from flask_socketio import SocketIO, send, emit, join_room, leave_room
from flask_login import current_user

socketio = SocketIO()

@socketio.on("message")
def handle_message(data):
    message = data["message"]
    room = data["room"]
    print(message + " sent to " + str(room))
    send(data, broadcast=True, to=room)

@socketio.on("join_room")
def join(data):
    room = data["room"]
    username = data["username"]
    join_room(room)
    emit("room response", f"{username} has joined the room " + room)

@socketio.on("leave_room")
def leave(data):
    room = data["room"]
    username = data["username"]
    leave_room(room)
    print(room, username)
    emit("room response", f"{username} has left the room " + room)