from urllib.request import urlopen

def get_viewers():
    link = 'https://tmi.twitch.tv/group/user/akabotsuo/chatters'
    f = urlopen(link)
    myfile = f.read()
    myfile = myfile.decode().split('\n')
    viewers = False
    list = []
    for fil in myfile:
        if viewers and ']' in fil:
            viewers = False

        if viewers:
            list.append(fil.replace('"', '').replace(',', '').replace(' ', ''))
            print(fil.replace('"', '').replace(',', ''))

        if 'viewers' in fil:
            viewers = True

    return list