import pyb
from pyb import Pin, ADC
from util import ledsOff, binLeds, translate


def readADC(pin, margin=5, delay=100):
    """
    pin: Pin() which is connected to potentiometers output
    ret: value between 0 - 4096
    """

    last = -1
    adc = ADC(pin)
    while True:
        a = adc.read()
        if last + margin < a or a < last - margin:
            yield a
            last = a
        pyb.delay(delay)


def printADC(*args,**kwargs):
    for v in readADC(*args, **kwargs):
        print(v)


def led4ADC(*args, **kwargs):
    led = pyb.LED(4)
    try:
        for v in readADC(*args, **kwargs):
            intensity = translate(v, nMax=255)
            led.intensity(intensity)
    finally:
        ledsOff()


def ledsADC(*args, **kwargs):
    leds = [pyb.LED(i) for i in range(1,5)]
    try:
        for v in readADC(*args, **kwargs):
            val = translate(v, nMax=16)
            binLeds(val, leds=leds)
    finally:
        ledsOff()


def extLedBlink(led=Pin('X2', Pin.OUT_PP),
                pot=ADC(Pin('X1', Pin.IN)),
                delayRange=(50, 1000)):
    """Blink an external LED and change the interval with a potentiometer.

    led: Pin() where the LED is located.
    pot: Pin() which is connected to the potentiometers output.
    delayRange: the range the LED's blinking interval can be.
    """
    try:
        while True:
            d = translate(pot.read(),
                          nMin=delayRange[0],
                          nMax=delayRange[1])
            led.value(not led.value())
            pyb.delay(d)
    finally:
        led.low()

