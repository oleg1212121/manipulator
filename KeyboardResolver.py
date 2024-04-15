import time
import pyautogui
from Settings.Options import coordinates, animation, settings, symbols


class Resolver:

    def __init__(self):
        print('Resolver ready')

    def resolve(self, symbol):
        if symbol in symbols:
            path, region, hotkey, confidence, grayscale = symbols[symbol]
            time.sleep(animation['fast_duration'])
            if region:
                region = coordinates['keyboard_region']

            if hotkey:
                pyautogui.keyDown(hotkey)
            print(settings['images_folder'] + path)
            icon = pyautogui.locateOnScreen(settings['images_folder'] + path, 5, region=region, confidence=confidence, grayscale=grayscale)

            # x, y = pyautogui.center(icon)
            pyautogui.moveTo(*pyautogui.center(icon), animation['pre_middle_duration'])
            time.sleep(animation['fast_duration'])
            pyautogui.click()

            if hotkey:
                pyautogui.keyUp(hotkey)
                time.sleep(animation['fast_duration'])
