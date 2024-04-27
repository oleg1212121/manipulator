import pyautogui
import time
import random
import winsound
from Settings.Options import *
from Settings.Credentials import credentials
from Logger import Logger


class PickBirthDate:

    def __init__(self):
        self.logger = Logger()

    def process(self):
        pyautogui.sleep(animation['middle_duration'])
        pyautogui.scroll(-800)

        # -----------------------------------------------------------------------
        # ---------------------   choose birthdate ------------------------------
        # -----------------------------------------------------------------------
        time.sleep(animation['pre_middle_duration'])
        icon = pyautogui.locateOnScreen('Images\\birthday.PNG', 5, grayscale=True, confidence=0.8)
        time.sleep(animation['fast_duration'])
        pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
        pyautogui.move(random.randint(-50, 50), 50, duration=animation['middle_duration'])
        pyautogui.tripleClick()
        pyautogui.press('delete')
        time.sleep(animation['pre_middle_duration'])
        pyautogui.write(credentials["birthday"], 0.2)
        time.sleep(animation['pre_middle_duration'])






