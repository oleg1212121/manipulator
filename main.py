import pyautogui
import time
import random
import winsound
from Login import Login
from Settings.Options import *
from MailReader import MailReader
from ApprovalLogin import ApprovalLogin
from CheckSlots import CheckSlots
from StartBrowser import StartBrowser
from LoginProcess import LoginProcess
from Logger import Logger

code = 'begin'
code = pyautogui.confirm(
    text=' BEGIN - full program\n LOGIN - starts from login menu\n CHECK_SLOTS - only change selected visa type',
    title='Which step?',
    buttons=['begin', 'login', "check_slots"]
)

while True:
    if code == 'begin':
        time.sleep(animation['short_sleep'])

        # start browser
        begin = StartBrowser()
        begin.process()
        code = 'login'

    if code in ['begin', 'login']:
        time.sleep(animation['middle_sleep'])

        # full login process
        login = LoginProcess()
        login.process()
        code = 'check_slots'

    if code in ['begin', 'login', 'check_slots']:
        time.sleep(animation['short_sleep'])
        checker = CheckSlots()
        checker.process()

        # refresh page
        # pyautogui.moveTo(*coordinates["refresh_button"], animation["middle_duration"], animation["animation"])
        # pyautogui.click()
        code = 'begin'
        logger = Logger()
        logger.log("Processing over. Sleeping for 10 minutes ...")
        time.sleep(900)
        logger.log("Processing will be restarted now...")