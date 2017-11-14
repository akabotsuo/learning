import socket

from Connection.Settings import HOST, PORT, PASS, IDENT, CHANNEL


def open_socket():

    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(("PASS " + PASS + "\r\n").encode())
    s.send(("NICK " + IDENT + "\r\n").encode())
    s.send(("JOIN #" + CHANNEL + "\r\n").encode())
    return s


def send_message(s, message):
    message_temp = "PRIVMSG #" + CHANNEL + " :" + message
    s.send((message_temp + "\r\n").encode())
    print("Sent: " + message_temp)
