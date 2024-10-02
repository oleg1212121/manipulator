from Manipulations.Assertions.CheckIfImageExists import CheckIfImageExists
import time


class CheckIfCookiesButtonReady:

    def __init__(self):
        self.check = CheckIfImageExists()

    def process(self):
        v = None
        for i in range(0, 10):
            try:
                print(f"try - {i}")
                v = self.check.check("cookies_button.PNG")
                if v:
                    print('FOUNDED')
                    break
            except:
                time.sleep(5)
                continue
        if not v:
            raise Exception("Cookies button doesn't appear")