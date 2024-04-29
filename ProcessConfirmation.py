import pyautogui
import time
import random
import winsound
from Settings.Options import *
from Settings.Credentials import credentials
from Logger import Logger


class ProcessConfirmation:

    def __init__(self):
        self.logger = Logger()
        self.title = 'Which step?'
        self.text = ' BEGIN - full program\n LOGIN - starts from login menu\n CHECK_SLOTS - only change selected visa type'

    def process(self, title=None, text=None):
        code = pyautogui.confirm(
            text=text or self.text,
            title=title or self.title,
            buttons=['begin', 'login', "check_slots", "pause", "sleep"]
        )
        return code




