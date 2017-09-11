from Connection.Socket import sendMessage

def joinRoom(s):
    readbuffer = ""
    Loading = True
    while Loading:
        readbuffer = readbuffer + s.recv(1024).decode()
        temp = str.split(readbuffer, "\n")
        readbuffer = temp.pop()

        for line in temp:
            print(line)
            Loading = loadingComplete(line)
    sendMessage(s, "Bot is now active")

def loadingComplete(line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True
