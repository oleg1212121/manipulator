import pyautogui
import time
import winsound
from KeyboardResolver import Resolver
from Settings.Options import coordinates, animation, approval_keyboard


class ApprovalLogin:


    def __init__(self):
        print('login ready')

    def process(self, numbers):
        # input email during login
        pyautogui.moveTo(*coordinates['approval_input'], animation['middle_duration'], animation['animation'])
        pyautogui.click()
        time.sleep(animation['middle_duration'])

        # input password during login
        pyautogui.moveTo(*approval_keyboard['backspace'], animation['middle_duration'])
        pyautogui.click()
        for i in range(0,6):
            pyautogui.click()
            time.sleep(animation['fast_duration'])

        for symbol in numbers:
            pyautogui.moveTo(*approval_keyboard[symbol], animation['middle_duration'])
            pyautogui.click()

        # input password during login
        pyautogui.moveTo(*coordinates['approval_submit'], animation['middle_duration'], animation['animation'])
        pyautogui.click()
        print('approval done')