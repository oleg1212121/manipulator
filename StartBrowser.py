import pyautogui
import time
import random
import winsound
from Settings.Options import *
from Logger import Logger
from TimeFiller import TimeFiller


class StartBrowser:

    def __init__(self):
        self.logger = Logger()
        self.filler = TimeFiller()

    def process(self):
        time.sleep(animation['short_sleep'])
        self.logger.log("Processing open browser...")
        # -----------------------------------------------------------------------
        # ---------------------   Start browser   -------------------------------
        # -----------------------------------------------------------------------
        # open browser
        time.sleep(animation['fast_duration'])
        pyautogui.click(coordinates["browser"])
        time.sleep(animation['slow_duration'])

        # resize browser
        pyautogui.hotkey('win', 'up')
        time.sleep(animation['fast_duration'])

        # create browser action history
        for link in settings['links']:
            pyautogui.hotkey("ctrl", "l")
            time.sleep(animation['pre_middle_duration'])
            pyautogui.press('backspace')
            time.sleep(animation['pre_middle_duration'])
            pyautogui.write(link)
            time.sleep(animation['pre_middle_duration'])
            pyautogui.press("enter")
            self.filler.shake(4)

        time.sleep(animation['middle_sleep'])



