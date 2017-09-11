from Connection.Initialize import joinRoom
from Connection.Ping import pong
from Connection.Read import getMessage
from Connection.Socket import openSocket
from ChatGame.CallCheck import check_call
s = openSocket()
joinRoom(s)
readbuffer = ""
pongN = 0
while True:
    readbuffer = readbuffer + s.recv(1024).decode()
    temp = str.split(readbuffer, "\n")
    readbuffer = temp.pop()


    for line in temp:
        print(line)
        if pong(line, s, pongN): pongN = pongN + 1
        else:
            if getMessage(line)[0] == '!':check_call(line,s)
