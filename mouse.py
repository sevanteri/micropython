import pyb

sw = pyb.Switch()
ac = pyb.Accel()

while not sw():
    pyb.hid((0, ac.x(), -ac.y(), 0))
    pyb.delay(20)
