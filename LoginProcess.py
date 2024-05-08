import pyautogui
import time
import random
import winsound
from Login import Login
from Settings.Options import *
from MailReader import MailReader
from ApprovalLogin import ApprovalLogin
from Logger import Logger


class LoginProcess:

    def __init__(self):
        self.logger = Logger()

    def process(self):
        time.sleep(animation['middle_sleep'])
        # -----------------------------------------------------------------------
        # ---------------------     LOGIN         -------------------------------
        # -----------------------------------------------------------------------
        login = Login()
        login.process()
        time.sleep(animation['short_sleep'])

        # -----------------------------------------------------------------------
        # ---------------------     Mail read     -------------------------------
        # -----------------------------------------------------------------------
        reader = MailReader()
        numbers = reader.process()

        # -----------------------------------------------------------------------
        # ---------------------     Approve code  -------------------------------
        # -----------------------------------------------------------------------
        approve = ApprovalLogin()
        approve.process(numbers)

        # -----------------------------------------------------------------------
        # ---------------  Click appointment button   ---------------------------
        # -----------------------------------------------------------------------
        pyautogui.moveTo(*coordinates['appointment_button'], animation['middle_duration'], animation['animation'])
        time.sleep(animation["middle_sleep"])
        pyautogui.click()