import pyautogui
import time
import random
import winsound
from Settings.Options import *
from Settings.Credentials import credentials
from Logger import Logger
from CheckSlotScenaries.PickCenter import PickCenter
from CheckSlotScenaries.PickCategory import PickCategory
from CheckSlotScenaries.PickSubCategory import PickSubCategory
from CheckSlotScenaries.PickBirthDate import PickBirthDate
from CheckSlotScenaries.PickCitizenship import PickCitizenship


class MinskShenghenCVisitsScenario:

    def __init__(self):
        self.logger = Logger()

    def process(self):
        # -----------------------------------------------------------------------
        # ---------------------   choose center   -------------------------------
        # -----------------------------------------------------------------------
        center = PickCenter()
        center.process('Images\\minsk_center.PNG')

        # -----------------------------------------------------------------------
        # ---------------------   choose category -------------------------------
        # -----------------------------------------------------------------------
        category = PickCategory()
        category.process('Images\\category_visa_c.PNG')

        # -----------------------------------------------------------------------
        # ---------------------   choose birthdate ------------------------------
        # -----------------------------------------------------------------------
        birthdate = PickBirthDate()
        birthdate.process()

        # -----------------------------------------------------------------------
        # ---------------------   choose citizenship ----------------------------
        # -----------------------------------------------------------------------
        citizenship = PickCitizenship()
        citizenship.process('Images\\citizenship_belarus.PNG')

        # -----------------------------------------------------------------------
        # ---------------------   choose subcategory ----------------------------
        # -----------------------------------------------------------------------
        subcategory = PickSubCategory()
        subcategory.process('Images\\subcategory_visa_c.PNG')





