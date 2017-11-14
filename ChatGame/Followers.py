import random

from Connection.Socket import send_message
from Connection.Read import get_user_line
from db.SQL import *


def follow_check(user):  # Returns true if u are allowed to follow
    if get_user("Followers", user) is not None:
        return True
    else:
        return False


def join(line, s):
    user_exist = get_player(line)
    print(user_exist)
    if get_user('Followers', user_exist) is not None:
        send_message(s, (user_exist + " you have already joined the " + get_user('Followers', user_exist)[2] + " team!"))
    else:
        follow(user_exist, s)


def get_player(line):
    user = get_user_line(line)
    return user


def get_user_points(user):
    print(get_user("Followers", user)[1])
    return get_user("Followers", user)[1]


def gain_points(user, points):
    update_points('Followers', user, get_user_points(user) + points)


def follow(user, s):
    team = random.choice(["Green", "Red"])
    send_message(s, (user + " joined the " + team + " team!"))
    new_follower('Followers', user, team)
