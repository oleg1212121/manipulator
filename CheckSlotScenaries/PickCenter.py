import pyautogui
import time
import random
import winsound
from Settings.Options import *
from Settings.Credentials import credentials
from Logger import Logger


class PickCenter:

    def __init__(self):
        self.logger = Logger()

    def process(self, image):
        pyautogui.sleep(animation['middle_duration'])
        pyautogui.scroll(800)

        # -----------------------------------------------------------------------
        # ---------------------   choose center   -------------------------------
        # -----------------------------------------------------------------------
        time.sleep(animation['middle_duration'])
        icon = pyautogui.locateOnScreen('Images\\choose_center.PNG', 5, grayscale=True, confidence=0.9)
        time.sleep(animation['middle_duration'])
        pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
        pyautogui.click()
        time.sleep(animation['middle_duration'])
        pyautogui.move(random.randint(-50, 50), 50, duration=animation['middle_duration'])
        pyautogui.click()
        pyautogui.scroll(400)

        # pick option
        time.sleep(animation['middle_duration'])
        for i in range(2):
            try:
                time.sleep(animation['middle_duration'])
                icon = pyautogui.locateOnScreen(image, 5, grayscale=True, confidence=0.9)
                time.sleep(animation['middle_duration'])
                pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
                pyautogui.click()
                break
            except:
                pyautogui.scroll(-200)




