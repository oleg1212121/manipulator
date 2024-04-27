import pyautogui
import time
import random
import winsound
from Settings.Options import *
from Settings.Credentials import credentials
from Logger import Logger


class PickCitizenship:

    def __init__(self):
        self.logger = Logger()

    def process(self, image):
        pyautogui.sleep(animation['middle_duration'])
        pyautogui.scroll(-800)

        # -----------------------------------------------------------------------
        # ---------------------   choose citizenship ----------------------------
        # -----------------------------------------------------------------------
        time.sleep(animation['pre_middle_duration'])
        icon = pyautogui.locateOnScreen('Images\\citizenship.PNG', 5, grayscale=True, confidence=0.8)
        time.sleep(animation['fast_duration'])
        pyautogui.moveTo(*pyautogui.center(icon), duration=animation['pre_middle_duration'])
        pyautogui.click()
        time.sleep(animation['pre_middle_duration'])
        pyautogui.move(random.randint(-50, 50), 50, duration=animation['pre_middle_duration'])
        pyautogui.click()

        time.sleep(animation['fast_duration'])
        pyautogui.scroll(3000)

        for i in range(20):
            try:
                time.sleep(animation['pre_middle_duration'])
                icon = pyautogui.locateOnScreen(image, 5, grayscale=True, confidence=0.8)
                time.sleep(animation['fast_duration'])
                pyautogui.moveTo(*pyautogui.center(icon), duration=animation['pre_middle_duration'])
                pyautogui.click()
                break
            except:
                pyautogui.scroll(-280)



