import time
import pyautogui
from Settings.settings import elements
from Manipulations.Assertions.CheckIfImageExists import CheckIfImageExists


class ConfirmApprovalForm:

    def __init__(self):
        self.check = CheckIfImageExists()

    def process(self):
        flag = False
        for i in range(0, 3):
            try:
                self.check.check("cloudflare_passed.PNG")
                flag = True
                break

            except:
                pyautogui.moveTo(*elements['coordinates']['approval_checkbox'],
                                 duration=elements['animation']['pre_middle_duration'])
                pyautogui.click()
                time.sleep(10)
                continue

        if not flag:
            raise Exception('Cloudflare failed')