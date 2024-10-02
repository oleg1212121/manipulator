
import time
import pyautogui
from Settings.settings import elements
from Manipulations.Assertions.CheckIfImageExists import CheckIfImageExists


class ClickApprovalSubmit:

    def __init__(self):
        self.check = CheckIfImageExists()

    def process(self):
        pyautogui.moveTo(*elements['coordinates']['approval_submit'], duration=elements['animation']['pre_middle_duration'])
        pyautogui.click()
