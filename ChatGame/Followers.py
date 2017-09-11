import random

from Connection.Socket import sendMessage
from Connection.Read import getUser


def join(line,s):
    userExist = get_player(line)

    if 0 < len(userExist[0]):
        sendMessage(s, (userExist[0] + " you have already joined the " + userExist[1]  + " team!"))
    else:
        follow(userExist[0],s)

    #Do luck func

def get_player(line):
    user = getUser(line)
    file = open("ChatGame\score", "r")
    i = 1
    koll = file.readlines(i)
    userExist = False

    while koll:
        Tuser = str(koll).split(" ", 3)[0].replace("['", "")
        if Tuser == user:
            file.close()
            return koll.split(" ")
        else:
            koll = file.readlines(i)

    file.close()
    return []


def gainPoints(user,points):
    file = open("score", "r")
    i = 1
    koll = file.readlines(i)
    userExist = False
    while koll:
        # print(koll)
        koll = str(koll)
        Tuser = koll.split(" ", 3)[0]
        Tuser = Tuser.replace("['", "")
        if Tuser == user:
            return False



def follow(user,s):
    team = random.choice(["Green", "Red"])
    sendMessage(s, (user + " joined the " + team + " team!"))
    file = open("score", "a")
    file.write(user + " " + team + " 0 -\n")
    file.close()

#ej klar
def fb(line,s,user,team,points):
    if points is int:
        if points > 1000 or points <= 0:
            return False
        #place bet if bet open send into function


