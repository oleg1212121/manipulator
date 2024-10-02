import pyautogui
import time
from Manipulations.KeyboardResolver.KeyboardResolver import Resolver
from Settings.settings import *
from Manipulations.Logger.Logger import Logger


class LoginProcess:

    def __init__(self):
        self.logger = Logger()

    def process(self):
        self.logger.log('Login started')

        # input email during login
        pyautogui.moveTo(*elements['coordinates']['email_input'], elements['animation']['pre_middle_duration'], elements['animation']['animation'])
        pyautogui.tripleClick()
        time.sleep(elements['animation']['pre_middle_duration'])
        pyautogui.press('delete')
        pyautogui.write(credentials['gmail']['email'], interval=elements['animation']['fast_duration'])

        # input password during login
        pyautogui.moveTo(*elements['coordinates']['password_input'], elements['animation']['middle_duration'], elements['animation']['animation'])
        pyautogui.click()
        time.sleep(elements['animation']['middle_duration'])
        resolver = Resolver()

        # resolver.resolve('backspace')
        # for i in range(0,14):
        #     pyautogui.click()
        #     time.sleep(animation['fast_duration'])

        for symbol in credentials['gmail']['password']:
            resolver.resolve(symbol)

