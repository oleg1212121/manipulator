import pyautogui
import time
import random
import winsound
from Settings.Options import *
from Settings.Credentials import credentials
from Logger import Logger

class CheckSlots:

    def __init__(self):
        self.logger = Logger()


    def process(self):

        for i in range(0, 10):
            self.logger.log('Checking slots started')
            # -----------------------------------------------------------------------
            # ---------------------   choose center   -------------------------------
            # -----------------------------------------------------------------------
            time.sleep(animation['pre_middle_duration'])
            icon = pyautogui.locateOnScreen('Images\\choose_center.PNG', 5, grayscale=True, confidence=0.8)
            time.sleep(animation['fast_duration'])
            pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
            pyautogui.click()
            time.sleep(animation['fast_duration'])
            pyautogui.move(random.randint(-50, 50), 50, duration=animation['middle_duration'])
            pyautogui.click()

            # scroll to option
            time.sleep(animation['pre_middle_duration'])
            pyautogui.scroll(-200)

            image = 'Images\\minsk_center.PNG'
            # change subcategory to other visits
            if i % 2 == 1:
                image = 'Images\\center_grodno.PNG'
            # pick option
            time.sleep(animation['pre_middle_duration'])
            icon = pyautogui.locateOnScreen(image, 5, grayscale=True, confidence=0.9)
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
            pyautogui.move(random.randint(-50, 50), 50, duration=animation['middle_duration'])
            pyautogui.click()

            # pick category
            time.sleep(animation['pre_middle_duration'])
            icon = pyautogui.locateOnScreen('Images\\category_visa_c.PNG', 5, grayscale=True, confidence=0.8)
            time.sleep(animation['fast_duration'])
            pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
            pyautogui.click()


            # -----------------------------------------------------------------------
            # ---------------------   choose birthdate ------------------------------
            # -----------------------------------------------------------------------
            # time.sleep(animation['pre_middle_duration'])
            # icon = pyautogui.locateOnScreen('Images\\birthday.PNG', 5, grayscale=True, confidence=0.8)
            # time.sleep(animation['fast_duration'])
            # pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
            # pyautogui.move(random.randint(-50, 50), 50, duration=animation['middle_duration'])
            # pyautogui.tripleClick()
            # pyautogui.press('delete')
            # pyautogui.write(credentials["birthday"], 0.1)

            # scroll to end of page
            pyautogui.scroll(-300)

            # -----------------------------------------------------------------------
            # ---------------------   choose citizenship ----------------------------
            # -----------------------------------------------------------------------
            time.sleep(animation['pre_middle_duration'])
            icon = pyautogui.locateOnScreen('Images\\citizenship.PNG', 5, grayscale=True, confidence=0.8)
            time.sleep(animation['fast_duration'])
            pyautogui.moveTo(*pyautogui.center(icon), duration=animation['pre_middle_duration'])
            pyautogui.move(random.randint(-50, 50), 50, duration=animation['pre_middle_duration'])
            pyautogui.click()

            # scroll to option
            time.sleep(animation['fast_duration'])
            pyautogui.scroll(-800)

            # pick option
            time.sleep(animation['pre_middle_duration'])
            icon = pyautogui.locateOnScreen('Images\\citizenship_belarus.PNG', 5, grayscale=True, confidence=0.8)
            time.sleep(animation['fast_duration'])
            pyautogui.moveTo(*pyautogui.center(icon), duration=animation['pre_middle_duration'])
            pyautogui.click()


        # for i in range(0, 14):
            # -----------------------------------------------------------------------
            # ---------------------   choose subcategory ----------------------------
            # -----------------------------------------------------------------------
            time.sleep(animation['middle_duration'])
            icon = pyautogui.locateOnScreen('Images\\choose_subcategory.PNG', 5, grayscale=True, confidence=0.8)
            time.sleep(animation['middle_duration'])
            pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
            pyautogui.move(random.randint(-50, 50), 50, duration=animation['slow_duration'])
            pyautogui.click()

            image = 'Images\\subcategory_visa_other_c.PNG'
            # change subcategory to other visits
            # if i % 2 == 1:
            #     image = 'Images\\subcategory_visa_c.PNG'

            # pick subcategory
            time.sleep(animation['slow_duration'])
            icon = pyautogui.locateOnScreen(image, 5, grayscale=True, confidence=0.8)
            time.sleep(animation['slow_duration'])
            pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
            pyautogui.click()

            self.logger.log(f"{i} - iteration completed...")
            print(f"{i} - iteration")

            # -----------------------------------------------------------------------
            # ---------------------   check if warning here -------------------------
            # -----------------------------------------------------------------------
            try:
                time.sleep(animation['fast_duration'])
                pyautogui.locateOnScreen('Images\\sorry_notice.PNG', 5, grayscale=True, confidence=0.8)
                time.sleep(animation['slow_duration'])
                # pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
            except:
                print('SORRY NOT FOUND, SO SLOTS AVAILABLE')
                for i in range(0, 3):
                    winsound.Beep(400, 800)
                    time.sleep(0.2)
                pyautogui.alert(text='AVAILABLE DATES!!!', title='SUCCESS', button='OK')

            time.sleep(random.randint(60,65))
            pyautogui.scroll(800)

        pyautogui.hotkey('alt', 'f4')
