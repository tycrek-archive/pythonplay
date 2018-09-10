# Author: Joshua Moore (tycrek)

from directkeys import PressKey,ReleaseKey,ReleaseAll,keydict
keylist = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890")

t_time = 0.09

'''
def straight():
##    if random.randrange(4) == 2:
##        ReleaseKey(W)
##    else:
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)

def left():
    PressKey(W)
    PressKey(A)
    #ReleaseKey(W)
    ReleaseKey(D)
    #ReleaseKey(A)
    time.sleep(t_time)
    ReleaseKey(A)

def right():
    PressKey(W)
    PressKey(D)
    ReleaseKey(A)
    #ReleaseKey(W)
    #ReleaseKey(D)
    time.sleep(t_time)
    ReleaseKey(D)
'''


def press_keys(keys):
    ReleaseAll()
    for keyindex in keys:
        key = keylist[keyindex]
        if key.isdigit():
            key = 'n' + key
        elif key == " ":
            key = "SPACE"
        keyhex = keydict[key]
        PressKey(keyhex)
    time.sleep(t_time)
    ReleaseAll()