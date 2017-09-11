from Connection.Read import getUser
from Connection.Socket import openSocket, sendMessage


def pong(line,s,pongN):
    if "PING" in line:
        user = getUser(line)
        if "tmi.twitch.tv" in user:
            pongN = pongN + 1
            print("Twitch Ping user: " + user)  # tmi.twitch.tv
            s.send((line.replace("PING", "PONG")).encode())
            print((line.replace("PING", "PONG")).encode())
            sendMessage(s, ("Ping Pong %d" % (pongN)))
            return True
        else:
            print("User " + user)
            sendMessage(s, ("Don't do that " + user + "!"))
            return False