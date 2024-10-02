import time
import pyautogui
from Settings.settings import elements
from Manipulations.Assertions.CheckIfImageExists import CheckIfImageExists


class ClickSubmitButton:

    def __init__(self):
        self.check = CheckIfImageExists()

    def process(self):

        for i in range(0,3):
            flag = False
            try:
                pyautogui.moveTo(*elements['coordinates']['login_submit'], duration=elements['animation']['pre_middle_duration'])
                pyautogui.click()

                flag = self.check.check("login_enter_title.PNG")

                return True
            except:
                if flag:
                    time.sleep(60)
                    continue
                else:
                    return True

        return False