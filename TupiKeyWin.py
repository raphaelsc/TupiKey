#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#
#                                       #
#       Project:                        #
#                                       #
#                                       #
#                                       #
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#

import os
import SendKeys
import win32api
import time
import re


def binar(letra):

    mudar = bin(ord(letra))
    binario = mudar.replace("b","")
    print binario
    return binario

def startkey(x):
    
    print x
    try:
        if x[0] == 0:
            
            numlock = """{NUMLOCK}"""
            SendKeys.SendKeys(numlock,pause=0)
            
        elif x[0] == 1:

            numlock = "none"
            
        if x[1] == 0:

            capslock = """{CAPSLOCK}"""
            SendKeys.SendKeys(capslock,pause=0)
        
        elif x[1] == 1:

            capslock = "none"

        if x[2] == 0:

            scrolllock = """{SCROLLLOCK}"""
            SendKeys.SendKeys(scrolllock,pause=0)
        
        elif x[2] == 1:

            scrollock = "none"

    except e:

        print(e)

       
        
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
        SendKeys.SendKeys(send,pause=0)
    elif x[0] == 0:
        ""
    if x[1] == 1:
        send = ("""{CAPSLOCK}""")
        SendKeys.SendKeys(send,pause=0)
    elif x[1] == 0:
        ""
    if x[2] == 1:
        send = ("""{SCROLLLOCK}""")
        SendKeys.SendKeys(send,pause=0)
    elif x[2] == 0:
        ""
    

def transmitir(x):
    print x
    k = len(x)
    
    try:
        for i in xrange(0,k):
            print x[i]
            if x[i] == 0:
                time.sleep(1)
            #else:
            #   SendKeys.SendKeys("""{NUMLOCK}""",pause=0)
            #   time.sleep(1)
    except NameError as e:
            print e
        
    

#startkey(getLED())
#time.sleep(1)
#closekey(getLED())
#time.sleep(1)
#startkey(getLED())
#time.sleep(1)
#closekey(getLED())


entrada = raw_input("")


#time.sleep(3)


transmitir(binar(entrada))





#print binar(entrada)
#send = ("""{NUMLOCK 0}{CAPSLOCK 0}{SCROLLLOCK 0}""")
#SendKeys.SendKeys(send,pause=0)

