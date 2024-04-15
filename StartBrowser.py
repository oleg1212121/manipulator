import pyautogui
import time
import random
import winsound
from Settings.Options import *


class StartBrowser:

    def __init__(self):
        print("StartBrowser")

    def process(self):
        # -----------------------------------------------------------------------
        # ---------------------   Start browser   -------------------------------
        # -----------------------------------------------------------------------
        # open browser
        pyautogui.click(coordinates["browser"])
        time.sleep(animation['fast_duration'])

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
            for i in range(0, 5):
                x, y = random.randint(200, 1800), random.randint(200, 1000)
                pyautogui.moveTo(x, y, animation['pre_middle_duration'], animation['animation'])

        # wait for "is human" check
        time.sleep(animation['middle_sleep'])

        # -----------------------------------------------------------------------
        # ---------------------   IS HUMAN CHECK  -------------------------------
        # -----------------------------------------------------------------------
        try:
            pyautogui.locateOnScreen(settings['login_not_robot'], 5, confidence=0.9, grayscale=True)
            for i in range(0, 3):
                winsound.Beep(200, 1000)
                time.sleep(0.2)

            pyautogui.alert(text='LOGIN TO VFS ASKS FOR NO ROBOT APPROVAL', title='YOU HAVE 30 SEC', button='OK')
            time.sleep(30)
        except:
            print('no robot check in vfs login')