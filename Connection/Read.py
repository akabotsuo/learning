def get_user_line(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user


def get_message(line):
    separate = line.split(":", 2)
    message = separate[2]
    return message


def get_bet(line):
    separate = line.split(" ", 3+2)
    bet = separate[5]
    return bet
