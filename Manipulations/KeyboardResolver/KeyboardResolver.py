import time
import pyautogui
from Settings.settings import *


class Resolver:

    def __init__(self):
        print('Resolver ready')

    def resolve(self, symbol):
        if symbol in elements['symbols']:
            path, region, hotkey, confidence, grayscale = elements['symbols'][symbol]
            time.sleep(elements['animation']['fast_duration'])
            if region:
                region = elements['coordinates']['keyboard_region']

            if hotkey:
                pyautogui.keyDown(hotkey)
            print(paths['images_folder'] + path)
            icon = pyautogui.locateOnScreen(paths['images_folder'] + path, 5, region=region, confidence=confidence, grayscale=grayscale)

            # x, y = pyautogui.center(icon)
            pyautogui.moveTo(*pyautogui.center(icon), elements['animation']['pre_middle_duration'])
            time.sleep(elements['animation']['fast_duration'])
            pyautogui.click()

            if hotkey:
                pyautogui.keyUp(hotkey)
                time.sleep(elements['animation']['fast_duration'])
