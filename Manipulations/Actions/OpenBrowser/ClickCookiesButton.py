import pyautogui
from Settings.settings import elements


class ClickCookiesButton:

    def __init__(self):
        pass

    def process(self):
        icon = pyautogui.locateOnScreen('Images\\cookies_button.PNG', 5, grayscale=True, confidence=0.9)
        pyautogui.moveTo(*pyautogui.center(icon), duration=elements['animation']['pre_middle_duration'])
        pyautogui.click()