import time
import random
from Settings.Elements.settings import *
from Manipulations.Logger.Logger import Logger


class PickSubCategory:

    def __init__(self):
        self.logger = Logger()

    def process(self, image):
        pyautogui.sleep(animation['middle_duration'])
        pyautogui.scroll(800)

        # -----------------------------------------------------------------------
        # ---------------------   choose subcategory ----------------------------
        # -----------------------------------------------------------------------
        time.sleep(animation['middle_duration'])
        icon = pyautogui.locateOnScreen('Images\\choose_subcategory.PNG', 5, grayscale=True, confidence=0.9)
        time.sleep(animation['middle_duration'])
        pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
        pyautogui.click()
        time.sleep(animation['middle_duration'])
        pyautogui.move(random.randint(-50, 50), 50, duration=animation['slow_duration'])
        pyautogui.click()

        # pick subcategory
        time.sleep(animation['middle_duration'])
        icon = pyautogui.locateOnScreen(image, 5, grayscale=True, confidence=0.9)
        time.sleep(animation['middle_duration'])
        pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
        pyautogui.click()




