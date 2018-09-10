# direct inputs
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
# Dicionary and New keys by Joshua Moore (tycrek)

import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

keydict = dict()

# Original
keydict['W'] = 0x11
keydict['A'] = 0x1E
keydict['S'] = 0x1F
keydict['D'] = 0x20

# New
keydict['n1']=0x02
keydict['n2']=0x03
keydict['n3']=0x04
keydict['n4']=0x05
keydict['n5']=0x06
keydict['n6']=0x07
keydict['n7']=0x08
keydict['n8']=0x09
keydict['n9']=0x0A
keydict['n0']=0x0B

keydict['Q']=0x10
keydict['E']=0x12
keydict['R']=0x13
keydict['T']=0x14
keydict['Y']=0x15
keydict['U']=0x16
keydict['I']=0x17
keydict['O']=0x18
keydict['P']=0x19
keydict['F']=0x21
keydict['G']=0x22
keydict['H']=0x23
keydict['J']=0x24
keydict['K']=0x25
keydict['L']=0x26
keydict['Z']=0x2C
keydict['X']=0x2D
keydict['C']=0x2E
keydict['V']=0x2F
keydict['B']=0x30
keydict['N']=0x31
keydict['M']=0x32
keydict['SPACE']=0x39


# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseAll():
	ReleaseKey(A)
	ReleaseKey(B)
	ReleaseKey(C)
	ReleaseKey(D)
	ReleaseKey(E)
	ReleaseKey(F)
	ReleaseKey(G)
	ReleaseKey(H)
	ReleaseKey(I)
	ReleaseKey(J)
	ReleaseKey(K)
	ReleaseKey(L)
	ReleaseKey(M)
	ReleaseKey(N)
	ReleaseKey(O)
	ReleaseKey(P)
	ReleaseKey(Q)
	ReleaseKey(R)
	ReleaseKey(S)
	ReleaseKey(T)
	ReleaseKey(U)
	ReleaseKey(V)
	ReleaseKey(W)
	ReleaseKey(X)
	ReleaseKey(Y)
	ReleaseKey(Z)
	ReleaseKey(SPACE)
	ReleaseKey(n0)
	ReleaseKey(n1)
	ReleaseKey(n2)
	ReleaseKey(n3)
	ReleaseKey(n4)
	ReleaseKey(n5)
	ReleaseKey(n6)
	ReleaseKey(n7)
	ReleaseKey(n8)
	ReleaseKey(n9)


if __name__ == '__main__':
    PressKey(0x11)
    time.sleep(1)
    ReleaseKey(0x11)
    time.sleep(1)