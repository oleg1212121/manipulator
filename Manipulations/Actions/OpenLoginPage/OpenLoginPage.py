import pyautogui
import time
from Settings.settings import paths


class OpenLoginPage:

    def __init__(self):
        pass

    def process(self):
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.5)
        pyautogui.press('delete')
        time.sleep(0.5)
        pyautogui.write(paths['vfs_log_url'])
        time.sleep(0.5)
        pyautogui.press('enter')