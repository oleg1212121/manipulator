import pyautogui
import time
from Manipulations.Assertions.CheckIfImageExists import CheckIfImageExists
from Settings.settings import elements

class CheckIfCloudflareReady:

    def __init__(self):
        self.check = CheckIfImageExists()

    def process(self):
        v = None
        for i in range(0, 10):
            try:
                print(f"try - {i}")
                v = self.check.check("cloudflare_passed.PNG")
                if v:
                    print('Cloudflare passed OK')
                    break
            except:
                pyautogui.moveTo(*elements['coordinates']['login_checkbox'], duration=1)
                pyautogui.click()
                time.sleep(5)
                continue
        if not v:
            raise Exception("Cloudflare passed wrong")