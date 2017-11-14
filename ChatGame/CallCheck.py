from Connection.Read import get_message
from Connection.Socket import send_message
from ChatGame.Followers import join, get_user_points, get_player


def check_call(line, s):

    call = str(get_message(line))

    if '!rank' + call[len(call)-1] == call:
        send_message(s, " Plat 3")

    if '!join' + call[len(call)-1] == call:
        join(line, s)
    if '!points' + call[len(call)-1] == call:
        send_message(s, str(get_user_points(get_player(line))))
