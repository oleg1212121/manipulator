import pyautogui
from Manipulations.Simulations.TimeFiller import TimeFiller

class ShakeAndClick:

    def __init__(self):
        self.filler = TimeFiller()

    def process(self, time=5):
        pyautogui.moveTo(300, 300, duration=0.5)
        pyautogui.click()
        self.filler.shake(time)
