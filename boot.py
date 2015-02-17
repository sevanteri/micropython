# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

import pyb
from util import *

# press the user switch to select what to do
sel = selector()
if sel == 0:
    pyb.main('main.py') # main script to run after this one
elif sel == 1:
    pyb.usb_mode('CDC+HID') # act as a serial device and a mouse
    pyb.main('mouse.py')
#elif sel == 1:
    #pyb.usb_mode('CDC+MSC') # act as a serial and a storage device
