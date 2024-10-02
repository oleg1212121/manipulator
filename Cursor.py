import time
from Settings.Elements.settings import *
from Manipulations.Simulations.TimeFiller import TimeFiller


filler = TimeFiller()
filler.wait(6.1)
filler.shake(3.7)
# filler.activity(5.4)



# 820,770 - obywatelstwo
while True:
    print(pyautogui.position())
    time.sleep(1)

