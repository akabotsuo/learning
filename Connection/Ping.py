from Connection.Read import get_user_line
from Connection.Socket import open_socket, send_message


def pong(line, s, pong_n):
    if 'PING' in line:
        user = get_user_line(line)
        if 'tmi.twitch.tv' in user:
            pong_n = pong_n + 1
            print('Twitch Ping user: ' + user)  # tmi.twitch.tv
            s.send((line.replace('PING', 'PONG')).encode())
            print((line.replace('PING', 'PONG')).encode())
            send_message(s, ("Ping Pong %d" % pong_n))
            return True
        else:
            print('User ' + user)
            send_message(s, ("Don't do that" + user + '!'))
            return False
