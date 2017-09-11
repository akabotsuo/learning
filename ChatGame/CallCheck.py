from Connection.Read import getMessage
from Connection.Socket import openSocket
from Connection.Socket import sendMessage
from ChatGame.Followers import join
def check_call(line,s):

    call = str(getMessage(line))

    if "!rank" + call[len(call)-1] == call:
        sendMessage(s," Plat 3")

    if "!join" + call[len(call)-1] == call:
        join(line,s)