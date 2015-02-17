import pyb
from pyb import Pin


def translate(val, oMin=0, oMax=4096, nMin=0, nMax=255):
    return int(((val * (nMax - nMin)) / (oMax - oMin)) + nMin)


def ledsOff():
    [pyb.LED(i).off() for i in range(1,5)]


def binLeds(n, leds = [pyb.LED(i) for i in range(1,5)]):
    l = len(leds)
    n = n % 2 ** l
    ledsOff()
    for i in range(l):
        if n & (2**i):
            leds[i].on()

def flashLeds(leds = [pyb.LED(i) for i in range(1,5)]):
    l = len(leds)
    for i in range(l):
        leds[(i-1)%l].off()
        leds[(i)%l].on()
        pyb.delay(25)
    leds[-1].off()


def selector(timeout=2):

    time = 0
    selection = 0

    sw = pyb.Switch()
    def f():
        time = time * 0
        selection = selection + 1
    sw.callback(f)

    tim = pyb.Timer(4, freq=1)
    def g(t):
        time = time + 1
    tim.callback(g)

    while True:
        if (time >= timeout):
            break
        binLeds(selection)
        pyb.delay(100)

    ledsOff()
    sw.callback(None)
    tim.callback(None)
    tim.deinit()

    if selection == 0:
        flashLeds()
    else:
        #flash leds x times
        x = 3
        while x:
            x -= 1
            pyb.delay(100)
            binLeds(selection)
            pyb.delay(100)
            ledsOff()

    return selection

