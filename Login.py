import pyautogui
import time
import winsound
from KeyboardResolver import Resolver
from Settings.Options import coordinates, animation, credentials


class Login:

    def __init__(self):
        print('login ready')

    def process(self):
        # input email during login
        pyautogui.moveTo(*coordinates['email_input'], animation['middle_duration'], animation['animation'])
        pyautogui.tripleClick()
        time.sleep(animation['middle_duration'])
        pyautogui.press('delete')
        pyautogui.write(credentials['email'], interval=animation['fast_duration'])

        # input password during login
        pyautogui.moveTo(*coordinates['password_input'], animation['middle_duration'], animation['animation'])
        pyautogui.click()
        time.sleep(animation['middle_duration'])
        resolver = Resolver()
        resolver.resolve('backspace')
        for i in range(0,14):
            pyautogui.click()
            time.sleep(animation['fast_duration'])

        for symbol in credentials['password']:
            resolver.resolve(symbol)

        # input password during login
        pyautogui.moveTo(*coordinates['login_submit'], animation['middle_duration'], animation['animation'])
        pyautogui.click()
