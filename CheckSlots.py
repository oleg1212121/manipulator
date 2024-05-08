import pyautogui
import time
import random
import winsound
from Settings.Options import *
from Settings.Credentials import credentials
from Logger import Logger
from TimeFiller import TimeFiller
from CheckSlotScenaries.MinskShenghenCOtherScenario import MinskShenghenCOtherScenario
from CheckSlotScenaries.MinskShenghenCVisitsScenario import MinskShenghenCVisitsScenario
from CheckSlotScenaries.GrodnoShenghenCOtherScenario import GrodnoShenghenCOtherScenario
from CheckSlotScenaries.MinskShenghenDOtherScenario import MinskShenghenDOtherScenario
from CheckSlotScenaries.MinskShenghenDPostalScenario import MinskShenghenDPostalScenario


class CheckSlots:

    def __init__(self):
        self.logger = Logger()
        self.filler = TimeFiller()

    def process(self):
        self.filler.shake(animation['short_sleep'])
        self.logger.log('Checking slots started')
        minsk_visits_c = MinskShenghenCVisitsScenario()
        minsk_other_c = MinskShenghenCOtherScenario()
        minsk_other_d = MinskShenghenDOtherScenario()
        minsk_postal_d = MinskShenghenDPostalScenario()
        grodno_other_c = GrodnoShenghenCOtherScenario()
        arr = [
            minsk_other_c,
            minsk_other_d,
            minsk_postal_d,
            grodno_other_c,
            minsk_other_c,
            minsk_other_d,
            minsk_postal_d,
            grodno_other_c,
            minsk_other_c,
            minsk_other_d,
            minsk_postal_d,
            grodno_other_c
        ]
        for i in range(0, 9):

            self.logger.log(f"{i} - iteration completed...")
            print(f"{i} - iteration")

            arr[i].process()

            # -----------------------------------------------------------------------
            # ---------------------   check if warning here -------------------------
            # -----------------------------------------------------------------------
            self.filler.shake(animation['slow_duration'])
            pyautogui.scroll(-1000)
            try:
                self.filler.shake(animation['middle_duration'])
                pyautogui.locateOnScreen('Images\\sorry_notice.PNG', 5, grayscale=True, confidence=0.8)
                self.filler.shake(animation['fast_duration'])
            except:
                for i in range(0, 3):
                    winsound.Beep(400, 800)
                    self.filler.wait(0.2)
                pyautogui.alert(text='AVAILABLE DATES!!!', title='SUCCESS', button='OK')

            self.filler.activity(41)
            self.filler.wait(random.randint(10, 20))



