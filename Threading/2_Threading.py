from time import *
from threading import Thread

def mybox(delayt):
    while True:
        print("........OPEN")
        sleep(delayt)
        print("........CLOSE")
        sleep(delayt)
def LED(delayt):
    while True:
        print("LED on")
        sleep(delayt)
        print("LED OFF")
        sleep(delayt)
Delayb=3
DelayL=2
boxthread = Thread(target=mybox,args=(Delayb,))
LEDthread = Thread(target=LED,args=(DelayL,))
boxthread.daemon=True
LEDthread.daemon=True
boxthread.start()
LEDthread.start()
while True:
    pass