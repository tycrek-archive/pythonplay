# Author: Joshua Moore (tycrek)

from directkeys import PressKey,ReleaseKey,ReleaseAll,keydict
import time
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


def press_keys(keys, last):
    #ReleaseAll()
    print(keys)
    for lkey in last:
        if lkey not in keys:
            key = keylist[lkey]
            if key.isdigit():
                key = 'n' + key
            elif key == " ":
                key = "SPACE"
            keyhex = keydict[key]
            ReleaseKey(keyhex)

    print("[", end='')
    for keyindex in keys:
        key = keylist[keyindex]
        print(key + ",", end='')
        if key.isdigit():
            key = 'n' + key
        elif key == " ":
            key = "SPACE"
        keyhex = keydict[key]
        PressKey(keyhex)
    print("\b]")
    time.sleep(t_time)
    #ReleaseAll()