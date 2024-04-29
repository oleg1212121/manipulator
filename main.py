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
from ProcessConfirmation import ProcessConfirmation

confirmation = ProcessConfirmation()
code = confirmation.process()

while True:
    if code == 'begin':
        try:
            begin = StartBrowser()
            begin.process()
            code = 'login'
        except:
            code = confirmation.process(title='START BROWSER WENT WRONG')

    if code in ['begin', 'login']:
        try:
            login = LoginProcess()
            login.process()
            code = 'check_slots'
        except:
            code = confirmation.process(title='LOGIN WENT WRONG')

    if code in ['begin', 'login', 'check_slots']:
        try:
            checker = CheckSlots()
            checker.process()
            code = 'pause'
        except:
            code = confirmation.process(title='CHECKING SLOTS WENT WRONG')

    if code in ["pause", 'begin', 'login', 'check_slots']:
        pyautogui.hotkey('alt', 'f4')
        logger = Logger()
        logger.log("Paused for some minutes ...")
        time.sleep(700)
        logger.log("Processing will be restarted now...")
        code = 'begin'

    if code in ["sleep"]:
        pyautogui.hotkey('alt', 'f4')
        logger = Logger()
        logger.log("Sleep 1 hour ...")
        time.sleep(3780)
        code = 'begin'
