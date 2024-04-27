import pyautogui
import time
import random
import winsound
from Settings.Options import *
from Settings.Credentials import credentials
from Logger import Logger
from CheckSlotScenaries.MinskShenghenCOtherScenario import MinskShenghenCOtherScenario
from CheckSlotScenaries.GrodnoShenghenCOtherScenario import GrodnoShenghenCOtherScenario

class CheckSlots:

    def __init__(self):
        self.logger = Logger()


    def process(self):
        time.sleep(animation['short_sleep'])
        self.logger.log('Checking slots started')
        arr = [
            MinskShenghenCOtherScenario(),
            GrodnoShenghenCOtherScenario(),
            MinskShenghenCOtherScenario(),
            GrodnoShenghenCOtherScenario(),
            MinskShenghenCOtherScenario(),
            GrodnoShenghenCOtherScenario(),
            MinskShenghenCOtherScenario(),
            GrodnoShenghenCOtherScenario(),
            MinskShenghenCOtherScenario(),
            GrodnoShenghenCOtherScenario(),
            MinskShenghenCOtherScenario(),
            GrodnoShenghenCOtherScenario(),
        ]
        for i in range(0, 12):

            self.logger.log(f"{i} - iteration completed...")
            print(f"{i} - iteration")
            try:
                arr[i].process()
            except:
                pyautogui.alert(text='CHECK SLOT FAILED', title='FAIL', button='OK')
            # -----------------------------------------------------------------------
            # ---------------------   check if warning here -------------------------
            # -----------------------------------------------------------------------
            pyautogui.sleep(animation['fast_duration'])
            pyautogui.scroll(-1000)
            try:
                time.sleep(animation['middle_duration'])
                pyautogui.locateOnScreen('Images\\sorry_notice.PNG', 5, grayscale=True, confidence=0.8)
                time.sleep(animation['slow_duration'])
                # pyautogui.moveTo(*pyautogui.center(icon), duration=animation['slow_duration'])
            except:
                print('SORRY NOT FOUND, SO SLOTS AVAILABLE')
                for i in range(0, 3):
                    winsound.Beep(400, 800)
                    time.sleep(0.2)
                pyautogui.alert(text='AVAILABLE DATES!!!', title='SUCCESS', button='OK')

            for i in range(0, 22):
                x, y = random.randint(200, 1800), random.randint(200, 1000)
                pyautogui.moveTo(x, y, animation['middle_duration'], animation['animation'])
            time.sleep(random.randint(30, 42))



