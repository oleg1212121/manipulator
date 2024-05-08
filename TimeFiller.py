import pyautogui
import time
import random
from Settings.Options import *


class TimeFiller:

    def __init__(self):
        pass

    def wait(self, seconds):
        time.sleep(seconds)

    def activity(self, seconds):
        position = pyautogui.position()
        dur = 1
        shakes = int(seconds // dur)
        for i in range(0, shakes - 1):
            x, y = random.randint(200, 1700), random.randint(200, 900)
            pyautogui.moveTo(x, y, dur, animation['animation'])
        pyautogui.moveTo(*position, dur, animation['animation'])
        self.wait(seconds - (shakes * dur))

    def shake(self, seconds):
        position = pyautogui.position()
        dur = 0.2
        shakes = int(seconds // dur)
        for i in range(0, shakes-1):
            x, y = random.randint(position[0], position[0]+100), random.randint(position[1], position[1]+100)
            pyautogui.moveTo(x, y, dur, animation['animation'])
        pyautogui.moveTo(*position, dur, animation['animation'])
        self.wait(seconds - (shakes * dur))
