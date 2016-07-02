#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#                                       #
#       Author: Thiago Salgado          #
#                                       #
#   Job: IT Security - UCAM CAMPOS      #
#                                       #
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

import os
import SendKeys
import win32api
import time


def binar(letra):

    if letra == "a":
        change = bin(ord(letra))
        numb = change.replace("b","")
        #keyboard = 
    elif letra == "b":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "c":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "d":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "e":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "f":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "g":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "h":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "i":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "j":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "k":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "l":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "m":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "n":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "o":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "p":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "q":
        change = bin(ord(letra))
        numb = change.replace("b","")   
    elif letra == "r":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "s":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "t":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "u":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "v":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "w":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "x":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "y":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "z":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "A":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "B":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "C":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "D":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "E":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "F":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "G":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "H":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "I":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "J":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "K":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "L":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "M":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "N":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "O":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "P":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "Q":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "R":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "S":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "T":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "U":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "V":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "W":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "X":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "Y":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "Z":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "1":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "2":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "3":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "4":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "5":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "6":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "7":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "8":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "9":
        change = bin(ord(letra))
        numb = change.replace("b","")
    elif letra == "0":
        change = bin(ord(letra))
        numb = change.replace("b","")
    return (numb)

def startkey(x):
    print x
    if x[0] == 0:
        #send = ("""{NUMLOCK}{CAPSLOCK}{SCROLLLOCK}""")
        numlock = "{NUMLOCK}"
    elif x[0] == 1:
        numlock = None
    if x[1] == 0:
        capslock = "{CAPSLOCK}"
        
    elif x[1] == 1:
        capslock = None
    if x[2] == 0:
        scrolllock = "{SCROLLLOCK}"
        
    elif x[2] == 1:
        scrollock = None

    
    k = ("\"\"\""+numlock+capslock+scrolllock+"\"\"\"")
    print k
    SendKeys.SendKeys(k,pause=0)
    
        
def getLED():
    
    num = win32api.GetKeyState(0x90)
    caps = win32api.GetKeyState(0x14)
    scroll= win32api.GetKeyState(0x91)
    k = (num,caps,scroll)
    return k

def closekey(x):
    if x[0] == 1:
        #send = ("""{NUMLOCK}{CAPSLOCK}{SCROLLLOCK}""")
        send = ("""{NUMLOCK}""")
        SendKeys.SendKeys(send)
    elif x[0] == 0:
        ""
    if x[1] == 1:
        send = ("""{CAPSLOCK}""")
        SendKeys.SendKeys(send)
    elif x[1] == 0:
        ""
    if x[2] == 1:
        send = ("""{SCROLLLOCK}""")
        SendKeys.SendKeys(send,pause=0)
    elif x[2] == 0:
        ""
    

startkey(getLED())
entrada = raw_input("")
time.sleep(3)
closekey(getLED())
print binar(entrada)
#send = ("""{NUMLOCK 0}{CAPSLOCK 0}{SCROLLLOCK 0}""")
#SendKeys.SendKeys(send,pause=0)

