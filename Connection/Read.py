def getUser(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user

def getMessage(line):
    separate = line.split(":", 2)
    message = separate[2]
    return message

def getBet(line):
    seperate = line.split(" ", 3+2)
    bet = seperate[5] #!fb
    #print(bet)
    #To do, check valid number (between 1-1000?)
    return bet

def getChamp(line):
    seperate = line.split(" ", 3 + 2)
    champ= seperate[4]  # !fb
    file = open("Champs","r")

    i = 1
    koll = file.readlines(i)
    while koll:
        #print(koll)
        koll = file.readlines(i)




    #print(champ)
    #     return champ #To do, lista med tta på champs som inte finnschamps som skall checkas/ får inte be