import pyautogui
import time
import random
import winsound
from Settings.Options import *


class CheckSlots:

    def __init__(self):
        print("Initializing CheckSlots...")


    def process(self):
        # -----------------------------------------------------------------------
        # ---------------------   choose center   -------------------------------
        # -----------------------------------------------------------------------
        time.sleep(animation['pre_middle_duration'])
        icon = pyautogui.locateOnScreen('Images\\choose_center.PNG', 5, grayscale=True, confidence=0.8)
        time.sleep(animation['fast_duration'])
        pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
        pyautogui.move(50, 50, duration=animation['middle_duration'])
        pyautogui.click()

        # scroll to option
        time.sleep(animation['pre_middle_duration'])
        pyautogui.scroll(-200)

        # pick option
        time.sleep(animation['pre_middle_duration'])
        icon = pyautogui.locateOnScreen('Images\\minsk_center.PNG', 5, grayscale=True, confidence=0.9)
        time.sleep(animation['fast_duration'])
        pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
        pyautogui.click()

        # -----------------------------------------------------------------------
        # ---------------------   choose category -------------------------------
        # -----------------------------------------------------------------------
        time.sleep(animation['pre_middle_duration'])
        icon = pyautogui.locateOnScreen('Images\\choose_category.PNG', 5, grayscale=True, confidence=0.8)
        time.sleep(animation['fast_duration'])
        pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
        pyautogui.move(50, 50, duration=animation['middle_duration'])
        pyautogui.click()

        # pick category
        time.sleep(animation['pre_middle_duration'])
        icon = pyautogui.locateOnScreen('Images\\category_visa_c.PNG', 5, grayscale=True, confidence=0.8)
        time.sleep(animation['fast_duration'])
        pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
        pyautogui.click()

        # -----------------------------------------------------------------------
        # ---------------------   choose subcategory ----------------------------
        # -----------------------------------------------------------------------
        time.sleep(animation['pre_middle_duration'])
        icon = pyautogui.locateOnScreen('Images\\choose_subcategory.PNG', 5, grayscale=True, confidence=0.8)
        time.sleep(animation['fast_duration'])
        pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
        pyautogui.move(50, 50, duration=animation['middle_duration'])
        pyautogui.click()

        # pick subcategory
        time.sleep(animation['pre_middle_duration'])
        icon = pyautogui.locateOnScreen('Images\\subcategory_visa_c.PNG', 5, grayscale=True, confidence=0.8)
        time.sleep(animation['fast_duration'])
        pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
        pyautogui.click()

        # -----------------------------------------------------------------------
        # ---------------------   choose birthdate ------------------------------
        # -----------------------------------------------------------------------
        time.sleep(animation['pre_middle_duration'])
        icon = pyautogui.locateOnScreen('Images\\birthday.PNG', 5, grayscale=True, confidence=0.8)
        time.sleep(animation['fast_duration'])
        pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
        pyautogui.move(50, 50, duration=animation['middle_duration'])
        pyautogui.tripleClick()
        pyautogui.press('delete')
        pyautogui.write(credentials["birthday"], 0.1)

        # scroll to end of page
        pyautogui.scroll(-300)

        # -----------------------------------------------------------------------
        # ---------------------   choose citizenship ----------------------------
        # -----------------------------------------------------------------------
        time.sleep(animation['pre_middle_duration'])
        icon = pyautogui.locateOnScreen('Images\\citizenship.PNG', 5, grayscale=True, confidence=0.8)
        time.sleep(animation['fast_duration'])
        pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
        pyautogui.move(50, 50, duration=animation['middle_duration'])
        pyautogui.click()

        # scroll to option
        time.sleep(animation['fast_duration'])
        pyautogui.scroll(-800)

        # pick option
        time.sleep(animation['pre_middle_duration'])
        icon = pyautogui.locateOnScreen('Images\\citizenship_belarus.PNG', 5, grayscale=True, confidence=0.8)
        time.sleep(animation['fast_duration'])
        pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
        pyautogui.click()

        # -----------------------------------------------------------------------
        # ---------------------   check if warning here -------------------------
        # -----------------------------------------------------------------------
        try:
            time.sleep(animation['pre_middle_duration'])
            pyautogui.locateOnScreen('Images\\sorry_notice.PNG', 5, grayscale=True, confidence=0.8)
            time.sleep(animation['fast_duration'])
            # pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
        except:
            print('SORRY NOT FOUND, SO SLOTS AVAILABLE')
            for i in range(0, 3):
                winsound.Beep(400, 800)
                time.sleep(0.2)
            pyautogui.alert(text='AVAILABLE DATES!!!', title='SUCCESS', button='OK')

        # -----------------------------------------------------------------------
        # ---------------------  restart settings  ------------------------------
        # -----------------------------------------------------------------------

        # scroll to begin of the page
        pyautogui.scroll(1000)

        # choose center
        time.sleep(animation['pre_middle_duration'])
        icon = pyautogui.locateOnScreen('Images\\choose_center.PNG', 5, grayscale=True, confidence=0.8)
        time.sleep(animation['fast_duration'])
        pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
        pyautogui.move(50, 50, duration=animation['middle_duration'])
        pyautogui.click()

        time.sleep(animation['pre_middle_duration'])
        pyautogui.scroll(300)

        # pick first option
        time.sleep(animation['pre_middle_duration'])
        icon = pyautogui.locateOnScreen('Images\\center_baranovichi.PNG', 5, grayscale=True, confidence=0.9)
        time.sleep(animation['fast_duration'])
        pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
        pyautogui.click()
