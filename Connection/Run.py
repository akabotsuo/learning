from Connection.Initialize import join_room
from Connection.Ping import pong
from Connection.Read import get_message
from Connection.Socket import open_socket
from ChatGame.CallCheck import check_call
from db.Manage import init_once
from url.read_twitch_viewers import get_viewers
from db.SQL import update_points

s = open_socket()
join_room(s)
read_buffer = ""
pongN = 0

inits = True
if inits:
    init_once()
    inits = False
    count = 0
while True:
    read_buffer = read_buffer + s.recv(1024).decode()
    temp = str.split(read_buffer, "\n")
    read_buffer = temp.pop()
    for line in temp:
        print(line)
        if pong(line, s, pongN):
            pongN = pongN + 1
        else:
            if get_message(line)[0] == '!':
                check_call(line, s)

    count += 1
    if count > 5:
        count = 0
        viewers = get_viewers()
        print('givet poäng')
        for viewer in viewers:
            update_points('Followers', viewer, 1)
